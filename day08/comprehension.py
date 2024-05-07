#comprehension
#[0~100] 리스트 출력
a =  [x for x in range(101)]
# "apple" => [a,p,p,l,e]
b = [x for x in "apple"]

c = [x for x in range(11)]

# 0~100 짝수를 제곱인 형태인 리스트
# [0,4,16,64,...]


# 조건부 comprehension
# 홀수는 10 짝수는 20
[x + 10 if x % 2 == 1  else x + 20 for x in range(101)]

fruits = ["apple", "banana", "kiwi", "grape", "orange"]
# 5글자 이하면 글자의 길이로 나타내고, 아니면 대문자화 하기
# [5, BANANA, 4, 5, ORANGE]
i = [len(x) if len(x) <= 5 else x.upper() for x in fruits]