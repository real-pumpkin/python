#1. 뉴스 기사를 스크랩 해오고,
# 유저가 입력한 단어를 뉴스기사에서 그 해당 단어를 모두 대문자화 시켜서
# 다시 보여주기.
news = """Israel's working assumption was that Hamas would not accept a ceasefire proposal that the Americans called "exceptionally generous". At first light, Israel warned Palestinians to flee the eastern side of Rafah, because of an imminent military operation."""

word = input("단어입력:")
newNews = news.replace(word, word.upper())
print(newNews)
# 영어기사를 스크랩해오고
# 단어사이에 🍎 넣고 출력하기

words = news.split(" ")
news1 = "🍔".join(words)
print(news1)