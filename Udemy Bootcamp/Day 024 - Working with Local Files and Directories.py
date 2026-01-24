# open, read, close 필요
file = open("day_24.txt")
content = file.read()
print(content)
file.close()

# with 신택스로 수동으로 close 해줄 필요 없음
with open("day_24.txt") as file:
    content = file.read()
    print(content)

# mode="a" append(뒤에 추가), mode="w"은 지우고 추가
with open("day_24.txt", mode="a") as file:
    file.write("\nNew text.")

# mode="w" 상태에서 폴더에 없는 파일 생성 가능
with open("new_file.txt", mode="w") as file:
    file.write("Hello World.")
