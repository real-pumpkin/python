fruits = ["apple", "bannana", "kiwi", "mango"]
numbers = [1,2,3,4,5]
mix = ["안녕", 1, "집에갈래", 2, True, []]
starbucks = [["아메리카노","라떼"],["주스", "에이드"],["빵", "케이크"]]
print(starbucks[0][1]) # 라떼
print(starbucks[2][0]) # 빵

print("kiwi"[0])
# "kiwi"[1] => i
#kiwi == fruits[2]
#print(fruits[1].upper())

#append[추가하다]
fruits.append("grape")
print(fruits)

# extend[확장하다]
fruits.extend(["strewberry", "orange"])
print(fruits)

#sort(정렬하다)
fruits.sort()
print(fruits)

#reverse(반대로 하다)
fruits.reverse()
print(fruits)

#pop[맨뒤에 있는거 뺴기, 튀다]
fruits.pop()
print(fruits)

#remove(제거하다)
fruits.remove("orange")
print(fruits)

#count
fruits.append("banana")
x = fruits.count("banana")
print(x)

# for 리스트는 요소를 하나씩 뺴준다.
for x in fruits:
    print(x)
    