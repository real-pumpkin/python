# - 입력: n:5
# - 결과 : 9 (1+ 3+ 5)
# - 입력 : n:6
# - 결과 : 56(2^2 + 4^2 + 6^2)
num = int(input("입력 :"))
result = 0
if num % 2 == 1:
    for x in range(num+1):
        if x % 2 == 1:
            result += x

else:
    for x in range(num + 1):
        if x % 2 == 0:
            result += x**2
print(result)

arr = [1,2,3]
k = int(input("입력:"))

newList = []
if k % 2 == 1:
    for x in arr:
        newList.append(x * k)

else:
    for x in arr:
        newList.append(x + k)
print(newList)
