#1. 정삼각형 넓이구하기
underSide = int(input("밑변 입력:"))
height = int(input("높이 입력:"))
print(f"정삼각형의 넓이는 {underSide * height * 0.5}입니다.")


#2. if활용
num = int(input("숫자입력 :"))
if num % 2 == 1 and num > 0:
    print("입력한 숫자는 양수이며 홀수입니다.")
else:
    print("입력한 숫자는 양수 또는 홀수가 아닙니다.")

#3. 과일이름에 'a' 포함?
fruit = input("사용자입력 :")
if 'a' in fruit:
    print("해당 과일 이름에 'a'가 포함되는군요!")
else:
    print("해당 과일 이름에 'a'가 포함되지 않는군요!")


