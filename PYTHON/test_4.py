"""
if문 정말 중요하다.

if문이 작동하기 위한 조건 => if문이 True인지 Flase

Boolean 불리안, 불린, 책에서 *불*
True, False

***** + 돼지꼬리 땡땡
= : 변수 선언할때 변수에 값을 할당한다는 의미로 사용된다.
== : 비교연산자 중에 하나로 왼쪽에 있는 값과 오른쪽에 있는 값을 비교해서 같은지 확인한다
!= : 비교연산자 중에 하나로 왼쪽에 있는 값과 오른쪽에 있는 값이 다른지를 확인한다
< : "작다"
> : "크다"
>= : "크거나 작다"

"""
# print(1 == 2) # 다르다 => False
# print(1 != 2) # 다르다 => True
# print(1 < 2) # 맞다 => True
# print(1 > 2) # 아니다 => False
# # print(1 <= 2) # 맞다 => True
# # print(1 >= 2) # #아니다 => False

# # print("윈도우" == "맥") #한글과 한글을 비교해도 비교 연산자가 동작한다.
# # print("윈도우" == "윈도우")
# print("윈도우" < "맥") # 10진 코드표 크기 비교 가능
# print("윈도우" > "맥")
# print("A" < "a") # 아스키 코드표, 10진수로 보면 A보다 a가 크다

# i = input("원하시는 기능을 입력해주세요(1.입금 / 2.출금 / 3.잔고확인)")

# # i <= 사용자가 원하는 기능이 들어가 있다 입금, 출금, 잔고확인

# if i == "입금":
#     money = int(input("입금 금액 : ")) #input을 통해서 입력받은 데이터는 모두 문자형이다.
#     print(f'{money}원 입금하시겠습니까?')
# elif i == "출금":
#     print("출금 기능입니다.")
# elif i == "잔고확인":
#     print("잔고확인 기능입니다.")
# else :
#     print("제공하지 않는 기능입니다. 입금, 출금, 잔고확인 중 선택해주세요.")


# Ture => not ture -=> False

# print(not 1==2)
"""
# ==========
# and "그리고" / or "또는"

and는 곱하기 / True 1 / False 0


or는 더하기 / True 1 / False 0
True and True  => 1 * 1 => 1 => True
True and False => 1 * 0 => 0 => False
False and True => 0 * 1 => 0 => False
False and False => 0 * 0 => 0 => False


or는 더하기 / True 1 / False 0
True or True  => 1 * 1 => 1 => True
True or False => 1 * 0 => 0 => True
False or True => 0 * 1 => 0 => True
False or False => 0 * 0 => 0 => False

# True and False
"""

print(True and True) 
print(True and False)
print(False and True)
print(False and False)
