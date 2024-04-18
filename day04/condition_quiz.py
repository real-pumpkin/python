#1. 정수를 입력받고
#양의 홀수, 양의 짝수, 0, 음의 홀수, 음의 짝수
#판별해주는 프로그램
# ex) -5 => 음의 홀수, 0 => 0, 3 => 양의 홀수

num = int(input("정수입력:"))

if num > 0:
    if num % 2 == 1:
        print("양의 홀수 입니다.")
    else:
        print("양의 짝수 입니다.")
elif num == 0:
    print("0입니다.")
else:
    if num % 2 == 1:
        print("음의 홀수 입니다.")
    else:
        print("음의 짝수 입니다.")

num = int(input("정수 입력:"))
isPositive = num > 0
isNegative = num < 0
isOdd = num % 2 == 1
isEven = num % 2 == 0
if isPositive and isOdd:
    print("양의 홀수 입니다.")
elif isPositive and isEven:
    print("양의 짝수 입니다.")
elif isNegative and isOdd:
    print("양의 홀수 입니다.")
elif isNegative and isEven:
    print("음의 짝수 입니다.")
else:
    print("0입니다.")

#2 좌표평면에서 위치 판별 프로그램
x = int(input("x축은:"))
y = int(input("y축은:"))
if x > 0 and y > 0:
    print("입력하신좌표는 1사분면입니다.")
elif x < 0 and y > 0:
    print("입력하신좌표는 2사분면입니다.")
elif x < 0 and y < 0:
    print("입력하신좌표는 3사분면입니다.")
elif x > 0 and y < 0:
    print("입력하신좌표는 4사분면입니다.")
elif x > 0 or x < 0 and y == 0:
    print("입력하신좌표는 x축에 위치합니다.")
elif x == 0 and y > 0 or y < 0:
    print("입력하신좌표는 y축에 위치합니다.")
else:
    print("원점에 위치합니다.")

#isXPositive = num > 0
#isYPositive = num > 0
#isXNegative = num < 0
#isYNegative = num < 0
#isXZero = num == 0
#isYZero = num == 0
#쓰는 방법도 있음

price = int(input("구매 금액:"))
if price >= 200000:
    print(f"구매 금액은 {price}원, 할인율은{20}%, 할인금액은{price*0.2}원, 총 결제 금액은 {price-price*0.2}원 입니다.")
elif price >= 100000:
    print(f"구매 금액은 {price}원, 할인율은{10}%, 할인금액은{price*0.1}원, 총 결제 금액은 {price-price*0.1}원 입니다.")
elif price >= 50000:
    print(f"구매 금액은 {price}원, 할인율은{5}%, 할인금액은{price*0.05}원, 총 결제 금액은 {price-price*0.05}원 입니다.")
else:
    print(f"구매 금액은 {price}원, 할인율은{0}%, 할인금액은{price*0}원, 총 결제 금액은 {price-price*0}원 입니다.")


