def splitEmail(email):
    arr = email.split("@")
    return {"user" : arr[0], "domain": arr[1]}
print(splitEmail("itKorea@naver.com"))


spellingList = list("mega")
spellingList.sort() # [a,e,g,m]
strSpell = "". join(spellingList) # list -> str 변환
print(strSpell)

spellingList = list("mega") # [m,e,g,a]
spellingList. sort() # [a,e,g,m]
result = "".join(spellingList) # list -> str
print(result)

def spellingMagic(word):
    spellingList = list(word) # [a,e,g,m]
    spellingList.sort() # list -> str 변환
    result = "". join(spellingList) # list -> str

    spellingList1 = list(word)
    spellingList1.reverse()
    result1 = "".join(spellingList) #
    return {"sorted":result, "reversed": result1}

print(spellingMagic("koreait"))

# 정수 n이 주어졌을 때, 홀수면 "odd" 짝수면 "even 을 돌려주는
# 함수 만들기
def oddEven(n):
    if n % 2 == 1:
        return "odd"
    else:
        return "even"


