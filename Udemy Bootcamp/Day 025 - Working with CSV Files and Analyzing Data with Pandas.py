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
# print(data["temp"])

# pandas > series는 column, pandas > dataframe은 table의 개념
print(type(data))
print(type(data["temp"]))

# dataframe/series API
ddic = data.to_dict()
print(ddic)

temp_list = data["temp"].to_list()
print(temp_list)

# avg1 = sum(temp_list)/len(temp_list)
# print(avg1)
print(data["temp"].mean())
print(data["temp"].max())

# get data in columns
print(data["condition"]) # DDIC 처럼 사용
print(data.condition)  # object 처럼 사용

# get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# celcius to farenheit
monday = data[data.day == "Monday"]
monday_temp = monday.temp
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

# Create dataframe from scratch
data_dict = {
    "Ticker": ["TSLA", "NVDA", "TSMC"],
    "Description": ["Tesla", "NVIDIA", "Taiwan Semiconductor"]
}

data = pandas.DataFrame(data_dict)
data.to_csv("Ticker.csv")

