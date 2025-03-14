dict_oz = {
    "name" : "지훈",
    "키" : 178,
    "몸무게" : 79,
    "나이" : 35,
    "직업" : "백수"
}
# #dict 변경하고싶을때
# dict_oz["name"]="예든"

# #값을 추가하고싶을때 ket="강아지 이름" / values = "청풍"

# dict_oz["강아지_이름"] = "청풍"

# del dict_oz["강아지_이름"]
# print(dict_oz["강아지_이름"]) #선언할때는 괄호지만 키값을 구할때는 대괄호

# key = input("찾고자하는 키 값을 입력해주세요. :")

# if key in dict_oz:
#     print(dict_oz[key]) #key 는 변수
# else:
#     dict_oz[key] = "청풍" #key, value를 추가해줘
#     print(dict_oz) #넣은 값을 출력해줘

# value = dict_oz.get("강아지_이름")
# print("value에 들어있는 값?", value)

for key in dict_oz: # 딕셔너리에서의  for문은 정확하게 값을 정해줘야한다 ex) key, value ..
    print(dict_oz[key])

#items() : 내장 메소드로 key, value 쌍으로 출력 가능
# for key, value in dict_oz.items():
#     print(key, value)

print(dict_oz.items()) # key와 value를 동시에  꺼내므로 tuple로 나온다.

x, y, z = 1, 2, 3