Subscripting - 문자열에서 특정 요소 추출
print("Hello"[0]) # 0부터 첫번재 문자열
print("Hello"[-1]) # -1은 마지막 문자열

Integer = Whole Number (정수)
print(123+456) #숫자는 아무것도 없이 숫자만 쓰면 됨
print(123_456_789) #천단위마다 콤마 찍듯 _를 넣으면 그냥 보기 편함. 컴퓨터는 _가 없는 것으로 판단

Float = Floating Point Number (소수점)
print(123.45)

Boolean
print(True) #대문자로 시작. 아무 기호 없이 사용
print(False)

type function (데이터 타입이 무엇인지 알려줌)
print(type("123")) <class 'str'>
print(type(123)) <class 'int'>
print(type(True)) <class 'bool'>
print(type(123.45)) <class 'float'>

Type Conversion / Type Casting
int()
float()
str()
bool()

int("123") # 문자열을 정수로 변환
print(int("123") + int("456"))

print("Number of letters in your name: " + str(int(len(input("Enter your name")))))
=
var1 = input("Enter your name")
var2 = len(var1)
print("Number of letters in your name: " + str(var2))

Mathematic Operation
(수학적 연산)
print(123 + 456)
print(3 - 1)
print(3 * 3)
print(14 / 7) # 나누기는 항상 소수점을 가져옴, 부동 float 타입으로 암시적 형변환 진행됨
print(14 // 7) # 암시적 형변환하지 않고 정수 타입을 가져옴. 맞아떨어지지 않아도 정수만 가져옴
print(2 ** 2) # 제곱

# PEMDAD (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
괄호, 지수, 곱셈, 나눗셈, 덧셈, 뺄셈

//Debugging Test
bmi = 84 / 1.65 ** 2
print(bmi)

Number Panipulation
print(int(bmi)) # 절사
print(round(bmi)) # 반올림
print(round(bmi, 2)) # 소수점 n째자리까지 반올림

Assingment Operation
(할당 연산자)

score = 0
score +,-,*,/= 1
print(score)

f-strings
score = 0
height = 180
is_winning = True

print(f"Your score is {score}, your height is {height}, and your winning is {is_winning}")

Project

print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $ ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
no_of_people = input("How many people to split the bill?")

tip_percent = float("1." + tip)
total_amount = int(total_bill) * tip_percent
per_person = round(total_amount / int(no_of_people), 2)

print(f"Each person should pay: ${per_person}")
# 아래도 가능
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = (tip / 100 * bill) + bill
bill_per_person = round(bill_with_tip / people, 2)

print(f"Each person should pay: ${bill_per_person}")














