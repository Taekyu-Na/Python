with open("weather_data.csv") as file:
    data = file.readlines()
    print(data)

import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)

# pandas 사용하기
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
print(data["temp"])
