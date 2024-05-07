# - 입력: word = "abc" , n =3
# - 결과 : "aaabbbccc"
word = input("단어 입력:")
count = int(input("횟수 입력:"))

newWord = ""
for x in word:
     newWord += x * count
print(newWord)


word = input("단어 입력:")
newWord = ""
for x in  "hello":
    if x in "aeiou":
        newWord += x.upper()
    else:
        newWord += x
print(newWord)

# 단어를 입력했을때
# 자음은 대문자화 해서 출력하기
# ex > hello -> HeLLo

word = input("단어 입력:")
newWord = ""
for x in word:
    if x not in "aeiou":
        newWord += x.upper()
    else:
        newWord += x
print(newWord)