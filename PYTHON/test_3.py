list_a = [1,2,3,4,5]
list_b = list(range(1,6))
list_a.append(7)
# list_c = []
# list_d = list() 

# print(list_a)
# print(list_b)

# 숫자 7 맨 마지막에 넣는 2가지 방법
#append, insert -> list_a.append() -> 메소드  , len(list_a) ->함수


# list_a.append("안녕")

# # list_a.append(["이게", "될까?"])

# print(list_a)

result = list_a + list_b  #-> 결과값을 만들어놔야함
list_a = [1,2,3,4,5]
list_b = [6,7,8,9,10]
list_a + list_b   #-> 원본데이터에 영향을 주지 않기 때문에 비파괴적이라고 표현
print(list_a .extend(list_b)) #list_a.expend() 원본데이터 영향 준다
print(list_a)

#파이썬은 메모리 공간이 2배씩 늘어놔기때문에 용량관리를 위해 명령어 적절하게 사용해야함

#요소 제거
list_a = [1,2,3,4,5]
# result = print(list_a.pop(0)) #공란은 자동적으로 -1로 지정되며, 제일 마지막 값을 반환함
# print(result)

del list_a[-1]
del list_a[2:4]
print(list_a)

list_a = [1,2,3,4,5,2,3]  #앞에 인덱스부터 하나씩 삭제됨,
list_a.remove(4)
print(list_a)

list_a=[1,2,4,0,3,4,5,4,4]
# print(list_a[::-1]) #[시작값, 4+1], [시작값, ,2] 2칸씩 건너뛴다
list_a.sort() #오름차순으로 정렬됨, 괄호안에 reverse=True 로 하면 역순임
list_a.sort(reverse=True)
print(list_a)

list_a=[1,2,4,0,3,4,5,4,4]
result = sorted(list_a) #sorted는 용량차지가 많고 정렬이 느리다
print(result)

list_a=[1,2,4,0,3,4,5,4,4]
print(0 in list_a)

list_a=[1,2,4,0,3,4,5,4,4]
if 0 in list_a: # in 그 값이 안에 있나요?
    print("있다")
else:
    print("없다")

list_a=[1,2,4,0,3,4,5,4,4]
if 0 not in list_a: #not in 그 값이 안에 없나요 ?
    print("있다")
else:
    print("없다")