#print,input,sum,len,max,min,...

#map(how, target): target을 바꿔주기

map(lambda x: x*2,[1,2,3]) # [2,4,6]

numList = [i for i in range(101)]
# [100,101,102,103,...200]
map(lambda x:x+100,numList)

# map : target을 바꿔줌
numList = [x for x in range(10)]
result = list(map(lambda x:x*2,numList))
print(result)

# filter: target을 필터링해줌
result1 = list(filter(lambda x:x%2 ==0,numList))
print(result1)

fruits = ["apple", "banana", "cherry", "kiwi"]
filter(lambda x:len(x) <= 5, fruits)
#알파벳 a가 포함 되어있는 것 살리기
filter(lambda x:'a' in x , fruits)

emailList = ["abc@naver.com", "mega@gmail.com", "korea@daum.net"]
# map => 유저아이디로 바꾸기
map(lambda x: x.split("@")[0],emailList)

import math
# 군인[객체] [변수들 + 함수]
# math[객체] [자연상수,파이 + 함수]
