# 제어문
# 실행 순서를 조작하는 문법
# 조건문
# if,else,elif
print("프로그램 시작!")
num = int(input("숫자 입력"))
if num > 0:
    print("입력하신 숫자는 양수입니다.")
print("프로그램 끝!")

# [프로그램 시작 ----프로그램 끝]
#1. 숫자 입력을 받고, 해당숫자가 100이면, 100을 입력하셨습니다.

print("프로그램 시작")
num = int(input("숫자를 입력"))
if num ==100:
    print("100을 입력하셨습니다.")
print("프로그램 끝")

#2. 숫자 입력을 받고, 해당 숫자가 20~30이면, 20에서 30사이의 숫자를 입력하셨습니다.
print("프로그램 시작")
num = int(input("숫자를 입력"))
if num > 20 and num < 30:
    print("20에서 30사이의 숫자를 입력하셨습니다.")
print("프로그램 끝")

#3. 숫자를 입력받고, 해당 숫자가 짝수이면, 짝수입니다~!
print("프로그램 시작")
num = int(input("숫자를 입력"))
if num %2 == 0:
    print("짝수입니다~!")
print("프로그램 끝")

# else
print("프로그램 시작!")
num = int(input("숫자입력:"))
if num >= 0:
    print("양수입니다.")
else:
    print("음수입니다.")
print("프로그램 끝!")

# 비밀번호 입력 프로그램
# ! and "IT 포함되면, 올바르게 비밀번호 입력하였습니다!
# ! and "IT 포함되지 않으면, 올바르게 비밀번호 입력하지 않았습니다!
print("프로그램 시작!")
password = (input("비밀번호 입력:"))
if "!" in password and "IT" in password :
    print("올바르게 입력하였습니다.")
else:
    print("올바르게 입력하지 않았습니다.")
print("프로그램 끝!")

# 홀수짝수 판별 프로그램
print("프로그램 시작!")
num = int(input("정수 입력:"))
if num % 2 == 0:
    print("짝수입니다~!")
else:
    print("홀수입니다~!")

print("프로그램 끝!")

# 비밀번호 설정
# '!' 포함되지 않고 첫번째 글자가 'a' or 'A'이어야만
# 비밀번호를 올바르게 설정
# 아니면 비밀번호 올바르게 설정하지 않았습니다.
print("프로그램 시작!")
password = input("패스워드를 입력:")

if not ('!' in password) and (password[0] == 'a' or password[0] == 'A'):
    print("비밀번호를 올바르게 설정하였습니다.")
else:
    print("비밀번호를 올바르게 설정하지 않았습니다.")
print("프로그램 끝!")