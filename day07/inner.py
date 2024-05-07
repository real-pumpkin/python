# "hello".upper() => HELLO
# [].append("사과") => ["사과"]
# print,input,str,list,int,float,list,bool,range,type


#length
# len : 문자열 또는 리스트의 길이를 알려주는 기능
print(len("hello"))
print(len("python"))
print(len([2,4,6,8,10]))  # 정답 : 5, 인덱스 갯수

# max, min
print(max([2,12,3,51,23,312,3312,11]))
print(min([2,12,3,51,23,312,3312,11]))

#sum
print(sum([1,2,3,4,5]))

#영어 기사 스크랩 해오고,
# 단어 길이가 6글자 이상
# 단어들만 출력하기
# hint : split()

news = """Mr Shah and his mother are among millions of Indians who will cast their ballots in the third phase of the general election on Tuesday, when 94 constituencies across 12 states go to the polls."""

words = news.split()
for x in words:
    if len(x) >= 6:
        print(x)


fruits = ["apple", "banana", "kiwi", "mango", "strewberry", "pineapple", "melon"]

#문자 길이가 5글자 이하이고 알파벳 a,e 가 포함되면 대문자로 출력
# 그게 아니면 그 과일의 문자 길이를 출력하는 프로그램
# -> APPLE, 6, 4, MANGO, ...
fruits = ["apple", "banana", "kiwi", "mango", "strewberry", "pineapple", "melon"]

for x in fruits:
    if len(x) <= 5 and ("a" in x and "e" in x):
        print(x.upper())
    else:
        print(len(x))

