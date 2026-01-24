file = open("day_24.txt")
content = file.read()
print(content)
file.close()

with open("day_24.txt") as file:
    content = file.read()
    print(content)
