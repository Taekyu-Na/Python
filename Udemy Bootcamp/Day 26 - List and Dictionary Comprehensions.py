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
