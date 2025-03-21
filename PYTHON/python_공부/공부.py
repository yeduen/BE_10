# # 형 변환
# int()
# float('1.5')  # int(float('1.5'))
# str(2)

# #산술연산자

# # % 나머지 print(5%2) >> 1
# # // 몫  print(5//2) >> 2
# # ** 거듭제곱 print(5**2) >> 25

# # == 같다 print(5==2) >> False
# # != 같지않다 print(5 !=2) True

# # and 둘다 참이면 True print(3<5 and 7<5) >> False
# # or 하나라도 참이면 True print(3<5 or 7<5) >>True
# # not 반전 print(not 3 < 5) >>False

# # in 포함 print('c' in 'cat') >>True
# # not in 미포함 print('c' not in 'cat') >> False

# # a = 1
# # b = -2
# # c = 0

# # print(bool(a))
# # print(bool(b))
# # print(bool(c))
# # print(bool(None))

# # #인덱스 , 슬라이싱

# # lang = ('Python')
# # print(lang[0])
# # print(lang[-1])
# # print(lang[1:])
# # print(lang[1:])
# # print(lang[:4])
# # print(lang[:])


# # #문자열 처리
# # snack = '꿀과배기'
# # two = '2개' 

# # juseyo = snack + two
# # juseyo += '주세요'
# # print(juseyo)

# # #길이
# # print(len(snack))

# # #문자열 메소드
# # letter = 'how are YOU'
# # print(letter.lower())   #>>모든걸 소문자로
# # print(letter.upper())   #>>모든걸 대문자로
# # print(letter.capitalize())   #>>앞글자만 대문자로
# # print(letter.title())   #>> 각 문자의 첫글자만 대문자로
# # print(letter.swapcase())   #>> 대소문자 스왑
# # print(letter.split()) # > 문자열 나누기
# # print(letter.count('how')) #> 'how'가 몇번 쓰였나 계산

# #문자열 메소드
# s = '..나도고등학교..' 
# print(s.strip('.')) #불필요한 것 삭제
# print(s.replace('고등학교', '고교')) # 문자열 변경
# print(s.find('학교')) # 인덱스 순서로 시작시점 알려줌
# print(s.center(12,'-')) # 12글자로 '-'을 채워줌

# #문자열 포맷
# apple ='사과'
# banana = '바나나'
# print('빨가면', apple, '맛있으면',banana)
# print(f'빨가면 {apple} 맛있으면 {banana}')

# #탈출문자
# # 큰따옴표 \"
# # 작은 따옴표 \'
# print('하지만\'나만 당할순 없지\'라는 생각에 \"엄청쉽지\"라고했다.')
# snack ='꿀꽈배기는\n너무\n맛있어요'
# print(snack)

# #리스트

# list = ['값1','값2','값3']
# print(list[0:2])
# print('값1' in list)
# print(len(list))
# list[0] = '값4'
# print(list)
# list.append('값5') #값 추가
# list.remove('값3') #값 삭제
# # list.insert(1,'값6')
# print(list)

# #추가 리스트 메소드
# # pop() : 원하는 위치(또는 마지막)의 값 삭제
# # clear() : 모든 값 삭제
# sort() 값 순서대로 정렬
# reverse() : 순서뒤집기
# copy() : 리스트복사
# # count() : 갯수 
# # index() : 위치

# #튜플
# # 튜플은 수정 불가
# tuple = (1, 2, 3, 4, 5)
# # 리스트랑 같은 메서드 사용가능, 수정만 불가
# # 튜플 언패킹
# tuple = (1, 2, 3, 4, 5)

# numbers = (1,2,3,4,5,6,7,8,9)
# (one, two, *others) = numbers # *other은 리스트 형태로 된다

# #set{}
# A = {'값1', '값2', '값3'}
# B = {'값4', '값4', '값3'}
# print(A.union(B)) # 합집합 B와 A를 더한거 공통된거 중복값 출현 안됨
# print(A.difference(B)) #차집합 B에서 A를 뺀거

# set1 = {1,2,3,4,5}
# set2 = {3,4,4,5,6,7}
# print(set1.intersection(set2)) #교집합

# #셋트는 순서가 보장되지않아 인덱스 적용 불가
# set1.add(6) #셋트에 추가
# print(set1)
# set2.remove(7) #셋트에서 삭제
# print(set2)
# # set1.clear() >> 안에 내용 삭제인데, del set1 이라고하면 완전삭제
 
 #딕셔너리
# #딕셔너리 = (key1:value1, key2:value2)
# person ={
#     '이름': '지훈',
#     '나이': 35,
#     '키' : 178
# }
# print(person['나이'])
# print(person['키'])
# print(person.get('몸무게')) #key 값이 없어서 None으로 출력
# person['최종학력'] = '대졸' #key와 value 추가
# person['키'] = 180 #수정
# person.update({'키':180, '몸무게':79}) #여러개 수정
# print(person)
# print(person.items()) # 모든 key값과 valye값이 나옴
# print(person.keys()) 
# print(person.values()) 

#튜플과 리스트 변환
my_tuple = ('오예스', '몽셀')
my_list = list(my_tuple)
my_list.append('초코파이')
my_tuple = tuple(my_list)
print(my_tuple)

my_list = ['오예스', '몽셀','초코파이','초코파이','초코파이']
my_set = set(my_list) 
my_list = list(my_set) #중복값 제거

my_list = ['오예스', '몽셀','초코파이','초코파이','초코파이']
my_dic = dict.fromkeys(my_list)
print(my_dic)
my_list = list(my_dic)
print(my_list)