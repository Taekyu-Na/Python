List Comprehension

# 기존 리스트 계산
numbers = [1, 2, 3]
new_list = []
for n in numbers:
  add_1 = n + 1
  new_list.append(add_1)

# List Comprehension은 한줄로 가능
numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]

# String도 활용 가능
name = "TK"
new_list = [letter for letter in name]

# Range도 활용 가능
new_num = [n * 2 for n in range(1, 5)]

Conditional List Comprehension
new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eugene", "Freddy"]
short_names = [name for name in names if len(name) <= 4]
# Upper Case는 new_item에 넣기
upper_names = [name.upper() for name in names if len(name) > 5]

# 제곱수 실습
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num*num for num in numbers]
print(squared_numbers)

# 짝수 필터링 실습
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)

# 데이터 중첩
with open("file1.txt") as file1:
    list1 = file1.readlines()
with open("file2.txt") as file2:
    list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]
print(result)

Dictionary Comprehension
new_dict = {new_key:new_value for item in list}
new_dict = {new_key:new_value for (key,value) in dict.items()}

Conditional Dictionary Comprehension
new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# 임의 점수 부여하기
names = ["Alex", "Beth", "Caroline", "Dave", "Eugene", "Freddy"]
import random
students_scores = {student:random.randint(1, 100) for student in names}
# 60점 이상인 학생만 추출하기
passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}

# 연습
names = ["Alex", "Beth", "Caroline", "Dave", "Eugene", "Freddy"]
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)
passed_students = {student:score for (student,score) in student_scores.items() if score >= 80 }
print(passed_students)
just = {student:score + 1 for student, score in student_scores.items()}
print(just)
value = {score: score + 1 for score in student_scores.values()}
print(value)

# Dictionary Comprehension 실습 (1)
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}

# Dictionary Comprehension 실습 (2)
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(cel * 9/5) + 32 for (day,cel) in weather_c.items()}
print(weather_f)

Looping through dictionary
student_dict = {
    "student" : ["TK", "Tboy"],
    "score" : [48, 87]
}

for (key, value) in student_dict.items():
    print(key)
    print(value)

Looping through dataframe
import pandas

student_df = pandas.DataFrame(student_dict)
# print(student_df)

for (key, value) in student_df.items():
    # print(key)
    print(value)

Looping through rows of a dataframe
for (index, row) in student_df.iterrows():
    print(row.student) # row는 series
  if row.student == "TK":
    print(row.score)

Project

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv") # CSV 파일을 DataFrame으로 로딩
# read_csv() 함수에서 1. 파일열고 2. CSV 파싱 3. 각 열을 Series로 생성
# 모든 Series 묶어 DataFrame 객체 생성

nato_dict = {row.letter:row.code for (index,row) in data.iterrows()} # DataFrame을 dictionary로 변환
# iterrows()는 이터레이터로 각 반복마다 튜플(index, row) 반환
# (index, row)로 튜플 언패킹. index는 DataFrame의 인덱스값이고 row는 해당 행 전체를 담은 Series 객체

user_name = input("What is your name?  ").upper()
final_list = [nato_dict[letter] for letter in user_name]
print(final_list)

# 복습
import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

user_input = input("What is your name?  ").upper()
final_list = [nato_dict[letter] for letter in user_input]
print(final_list)
