# data-type : int,str,float, bool, list
# list. set(집합)
# 중복 허용 안되는 타입

a= {1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8}
burgerking = {"새우와퍼", "불고기와퍼", "치즈와퍼", "스테이크와퍼"}
momstouch = {"새우와퍼", "치즈와퍼", "싸이버거", "불고기버거"}

x = burgerking.intersection(momstouch)
print(x)

#합집합(|)
union = burgerking | momstouch

#교집합(&)
intersection = burgerking & momstouch
intersection1 = burgerking.intersection((momstouch))

#차집합 (-)
difference = burgerking - momstouch

print(union)
print(intersection)
print(difference)

# 추가
burgerking.add("새우와퍼")

# 삭제
burgerking.remove("새우와퍼") # 구문법 없는 요소 빼면 에러
burgerking.discard("새우와퍼") # 신문법 없는 요소 빼면 에러발생 안함

# 전체삭제
burgerking.clear()

# set()
result = set([1,2,3,1,2,3])
print(list(result))


news = """Astronauts Butch Wilmore and Suni Williams were already in position inside the Starliner when the decision to halt was made because of a potential issue with an oxygen relief valve."""

wordList = news.split()
noDuplicationWords = list(set(wordList))
noDuplicationWords.sort()
print(noDuplicationWords)