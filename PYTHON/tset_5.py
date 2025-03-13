# # 숫자를 입력받고 -> 음수, 양수, 0인지 구분하는 프로그램
# # 음수 < 0, 양수 > 0, 0 은 0

# number = input("정수를 입력해라")
# number = int(number) 

# # 양수조건
# if number > 0:
#     print("양수")
# # 음수조건
# if number < 0:
#     print("음수")
# # 0인 조건
# if number == 0:
#     print("0") #sep="" -> "" 사이에 넣으면 , 사이에 넣어짐 \ end="" 줄바꿈없이 일렬로 정렬

# len() # -> ? -> 길이를 구해줌

# import datetime #집합 이름, datetime을 실행시키려면 import 써야함.

# now = datetime.datetime.now()

# #1월~3월까지 봄입니다. -> 4월 ~ 8월 여름 -> 10월가지 가을 -> 11월 ~ 1월까지 겨울
# #if문으로만 해결

# month = int(input("월을 입력 (1~12):"))

# if 2 <= now.month <= 3:
#     print("봄")

# if 4 <= now.month and now.month <= 8:
#     print("여름")

# if 9 <= now.month <= 10:
#     print("가을")
# # 11월 ~ 1월
# if 11<= now.month or 1 == now.month:
#     print("겨울")


# print(now)
# print(now.year,"년")
# print(now.month,"월")
# print(now.day,"일")
# print(now.hour,"시")
# print(now.minute, "분")
# print(now.second,"초")

# number = input("정수 입력") # 1234 입력
# #1234 : str 시퀀스 타입, 순서가 있어 index
# last_number = number[-1]
# # 4:str -> 4:int
# last_number = int(last_number)
# # 4 : ini

# #짝수 인지르 확인하는 코드를 만들어주는데 if만 사용하고 or 연산자르 이용해서 짝수인지 확인해주세요
# #입력받은 숫자의 가장 마지막 값에 대해 짝수인지를 확인해주면됨.
# if last_number == 0 \
#     or last_number == 2 \
#     or last_number == 4 \
#     or last_number == 6 \
#     or last_number == 8:
#     print("짝수")

# if last_number == 1 \
#     or last_number == 3 \
#     or last_number == 5 \
#     or last_number == 7 \
#     or last_number == 9:
#     print("홀수")

# in을 써서 문제 해결 

# number = input("정수 입력") # 1234 입력
# last_number = number[-1]
# if last_number in "02468":
#     print("짝수")
# else:
#     print("홀수")

# number = input("정수 입력") # 1234 입력
# number = int(number)
# if number % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

#while ->
num = 0
while True: #while 문의 단점 무한 반복
    if num < 10:
        print("안녕", num)
    else:
        break
    num += 1
print("여기")
