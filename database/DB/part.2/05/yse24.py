from selenium.webdriver.common.by import By

from selenium import webdriver
browser = webdriver.Chrome()
browser.find_element(By.CLASS_NAME, 'uU7dJb').text




# 기존 세션이 만료되었을 수 있으므로 새로 생성


# URL 이동
url = 'https://www.yes24.com/product/category/bestseller?CategoryNumber=001&sumgb=06'
browser.get(url)

browser.find_element(By.CLASS_NAME, 'gd_name').get_attribute('herf')

## 1페이지 전체 수집
# browser.find_element(By.CLASS_NAME, 'gd_name') # element : 요소
datas = browser.find_elements(By.CLASS_NAME, 'gd_name') # elements : 리스트

for i in datas:
    print(i.get_attribute('href'))

import time

link_list = []
for i in range(1,4):
    print("*"*10,f"현재 {i}페이지 수집 중 입니다","*"*10)
    url = f'https://www.yes24.com/product/category/bestseller?categoryNumber=001&pageNumber={i}&pageSize=24'
    browser.get(url)
    browser.find_element(By.CLASS_NAME, 'gd_name').get_attribute('herf')

## 1페이지 전체 수집
# browser.find_element(By.CLASS_NAME, 'gd_name') # element : 요소
    datas = browser.find_elements(By.CLASS_NAME, 'gd_name') # elements : 리스트

    for i in datas:
        link = i.get_attribute('href')
        link_list.append(link)
    time.sleep(3)

print(link_list)


browser.get(link_list[0])

title = browser.find_element(By.CLASS_NAME, 'gd_name').text
author = browser.find_element(By.CLASS_NAME, 'gd_auth').text
publisher = browser.find_element(By.CLASS_NAME, 'gd_pub').text
publishing = browser.find_element(By.CLASS_NAME, 'gd_date').text
rating = browser.find_element(By.CLASS_NAME, 'yes_b').text
review = browser.find_element(By.CLASS_NAME, 'txC_blue').text
sales = browser.find_element(By.CLASS_NAME, 'gd_sellNum').text.split(" ")[2]
price = browser.find_element(By.CLASS_NAME, 'yes_m').text[:-1]
ranking = browser.find_element(By.CLASS_NAME, 'gd_best').text.split(" | ")[0]


title, author, publisher, publishing, rating, review, sales, price, ranking,




import pymysql
import time
import re
from datetime import datetime

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='2925',
    db='yes24',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with conn.cursor() as cur:
    
    for link in link_list:
        brower.get(link)

        title = browser.find_element(By.CLASS_NAME, 'gd_name').text
        author = browser.find_element(By.CLASS_NAME, 'gd_auth').text
        publisher = browser.find_element(By.CLASS_NAME, 'gd_pub').text

        publishing = browser.find_element(By.CLASS_NAME, 'gd_date').text

        match = re.search(r'(\d+)년 (\d+)월 (\d+)일', publishing)

        if match:
            year, month, day = match.groups()
            data_obj = datatime(int(year), int(month), int(day))
            publishing = data+obj.strftime("%y-%m-%d")
        else:
            publishing = "2023-01-01"

        rating = browser.find_element(By.CLASS_NAME, 'yes_b').text

        review = browser.find_element(By.CLASS_NAME, 'txC_blue').text
        review = int(review.replace(",",""))

        sales = browser.find_element(By.CLASS_NAME, 'gd_sellNum').text.split(" ")[2]
        sales = int(sales.replace(",",""))

        price = browser.find_element(By.CLASS_NAME, 'yes_m').text[:-1]
        price = int(price.replace(",",""))

        full_text = browser.find_element(By.CLASS_NAME, 'gd_best')
        parts - full_text.Split(" | ")
        try:
            ranking_part = parts[0]
            ranking = ''.koing(filter(str.isdigit, ranking_part))

        except:
            ranking = 0
       
        ranking = browser.find_element(By.CLASS_NAME, 'gd_best').text.split(" | ")[0]
        
        sql = """INSERT INTO Books(title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks)
        VALUES(
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)
        
        """

        cur.execute(sql,(title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks))
        conn.commit()
        time.sleep(2)