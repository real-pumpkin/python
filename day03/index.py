# 산술, 비교, 대입, 논리 ->기본
# 멤버쉽 연산자[in]
coffee = "americano"
print('a' in coffee) # True
print('ameri' in coffee) # True
text = """""" # 두 문장 이상의 글
news = """이번 총선을 통해 나타난 민심을 우리 모두 겸허하게 받아들여야 합니다. 더 낮은 자세와 유연한 태도로 보다 많이 소통하고 저부터 민심을 경청하겠습니다. 국민께서 바라시는 변화가 무엇인지, 어떤 것이 국민과 나라를 위한 길인지 더 깊이 고민하고 살피겠습니다. 민생을 위한 것이라면 어떠한 일도 마다하지 않을 것입니다."""
print("총선" in news)

# 슬라이싱 연산자 [:]
car = "tesla"
print(car[0:3]) # tes 0은 포함 3은 빼기
print(car[1:3]) # es

# 인덱스 연산자 [[]]
code = "python"
print(code[0]) # p
print(code[3]) # h

