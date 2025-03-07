#변수 선언 -> 변수에다가 우리가 원할때마다 계속 불러오고 싶은 데이터를 저장 -> 원할때마다 데이터 소환
# 왼쪽 변수명 "=" 오른쪽 변수에다가 집어넣고 싶은 값
# a = 1 => a라는 변수명에 숫자 1을 할당한다

# 회원가입 프로그램 만들기 -> 아이디, 비밀번호, 이름, 나이, 주소, 핸드폰 번호 -> 개인정보 -> 데이터 
# 웹 프로그램의 핵심 -> 데이터를 처리하는 것 -> 숫자, 행동, 마우스클릭 -> 키보드 입력
# 숫자, 문자열, boolean(참,거짓 / yes or no / True or False)

#" " ' ' => 문자형

print(type(0))
print(type(0.0))
print(type("안녕하세요"))

print(0) # 문자자료형의 0으로 만들어
print(str(0)) # str() -> 데이터 타입을 문자형태로 바꿔주는 내장함수
print("0")
print('0') # 자료형태를 선언하지 않고 그냥 변수에 데이터를 넣어서 그냥 씀 -> 동적할당 ->값을 넣는 순간 데이터 타입을 정해줌

a = 100
b = 100
c = 200
print(id(a))
print(id(b))
print(id(c))

# len() -> 길이를 알려줌 ->인덱스는 0부터 시작이니때문에 하나가 짧다

# 시퀀스 순서가 생겼다 -> 슬라이싱 -> 인덱스라는걸 갖고 있으면 위치를 지정해서 마무잡이로 잘라 사용 가능

name = "asdasd"
print(name[1:4]) #슬라이싱 특징은 항상 마지막에 출력하고 싶어하는 인덱스보다 +1

import requests

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색할 키워드 입력 : ")

url = base_url + keyword
print(url)

req = requests.get(url)
print(req.text)