import requests 
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=%EC%9D%B4%EC%A0%95%ED%9B%84&qdt=0&ie=utf8&query=이정후"
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, "html.parser")

result = soup.select(".view_wrap")  # 결과는 리스트

for i in result:
    title_tag = i.select_one(".title_link")
    writer_tag = i.select_one(".info_group .name")  # 작성자 클래스는 상황에 따라 다름
    dsc_tag = i.select_one(".dsc_wrap")  # 설명 클래스도 바뀔 수 있음

    title = title_tag.text.strip() if title_tag else "제목 없음"
    writer = writer_tag.text.strip() if writer_tag else "작성자 없음"
    dsc = dsc_tag.text.strip() if dsc_tag else "요약 없음"

    print(f"제목 : {title}")
    print(f"작성자 : {writer}")
    print(f"글요약 : {dsc}")
    print("-" * 50)