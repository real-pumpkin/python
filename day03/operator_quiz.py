#operator_quiz
news = """대통령실이 조직개편을 논의하고 있는데요. '법률수석실'을 새로 만드는 방안이 검토되고 있단 보도가 있었죠.
일각에선 민정수석실의 부활 아니냐는 시각도 있고요. 신설되는 건가요?"""

word = input("검색하신 단어는 :")

result = word in news
print(f"검색하신 단어는 뉴스기사 내에서 {result}")

password = input("비밀번호 입력:")
result = "!" in password and "IT" in password
print(f"비밀번호가 요구사항을 {result}")