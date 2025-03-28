from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymysql
import time
import re
from datetime import datetime

# 웹드라이버 실행
browser = webdriver.Chrome()

# 베스트셀러 페이지 이동
base_url = "https://www.yes24.com/product/category/bestseller?categoryNumber=001&pageNumber={}&pageSize=24"

link_list = []
for i in range(1, 4):  # 1~3페이지 수집
    print(f"{'*' * 10} 현재 {i}페이지 수집 중 {'*' * 10}")
    browser.get(base_url.format(i))

    # 대기 후 책 링크 가져오기
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gd_name")))
    datas = browser.find_elements(By.CLASS_NAME, "gd_name")

    for data in datas:
        link = data.get_attribute("href")
        if link:
            link_list.append(link)
    time.sleep(3)

print("총 수집된 링크 개수:", len(link_list))

# MySQL 연결
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="2925",
    db="yes24",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

with conn.cursor() as cur:
    for link in link_list:
        browser.get(link)

        try:
            # 요소가 로드될 때까지 대기 후 데이터 추출
            title = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "gd_name"))
            ).text
            author = browser.find_element(By.CLASS_NAME, "gd_auth").text
            publisher = browser.find_element(By.CLASS_NAME, "gd_pub").text
            publishing = browser.find_element(By.CLASS_NAME, "gd_date").text

            # 출판일 변환
            match = re.search(r"(\d+)년 (\d+)월 (\d+)일", publishing)
            if match:
                year, month, day = match.groups()
                data_obj = datetime(int(year), int(month), int(day))
                publishing = data_obj.strftime("%Y-%m-%d")
            else:
                publishing = "2023-01-01"

            rating = browser.find_element(By.CLASS_NAME, "yes_b").text
            review = int(browser.find_element(By.CLASS_NAME, "txC_blue").text.replace(",", ""))
            sales = int(browser.find_element(By.CLASS_NAME, "gd_sellNum").text.split(" ")[2].replace(",", ""))
            price = int(browser.find_element(By.CLASS_NAME, "yes_m").text[:-1].replace(",", ""))

            # 랭킹 정보 추출
            try:
                full_text = browser.find_element(By.CLASS_NAME, "gd_best").text
                parts = full_text.split(" | ")
                ranking = int("".join(filter(str.isdigit, parts[0])))
            except:
                ranking = 0

            ranking_weeks = 0  # 랭킹 유지 기간이 없으므로 0으로 설정

            # 데이터베이스 저장
            sql = """
                INSERT INTO Books (title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(sql, (title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks))
            conn.commit()
            time.sleep(2)

        except Exception as e:
            print(f"오류 발생: {e}")
            continue

# 브라우저 및 데이터베이스 연결 종료
browser.quit()
conn.close()
