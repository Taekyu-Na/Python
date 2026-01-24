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

# Central Park Squirrel Analysis
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_list = data["Primary Fur Color"].to_list()
gray_count = color_list.count("Gray")

dictionary = {
    "Fur Color": [],
    "Count": []
}

fur_color = []
for row in data["Primary Fur Color"]:
    if row not in fur_color:
        fur_color.append(row)
        dictionary["Fur Color"].append(row)

for color in fur_color:
    each_count = color_list.count(color)
    dictionary["Count"].append(each_count)

data = pandas.DataFrame(dictionary)
data.to_csv("squirrel_count.csv")

# 선생님 답
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count_answer")

# 연습하기
df = pandas.read_csv("50_states.csv")

def get_axis():
    should_continue = True

    while should_continue == True:
        user_input = input("Choose a state to get the axis.:  ").title()
        record = df[df.state == user_input]
        var_x = int(record.x.values[0])
        var_y = int(record.y.values[0])
        print(f"{user_input}'s x: {var_x}, y: {var_y}")
        while should_continue == True:
            another_one = input("Choose another state to get axis. Or type 'no' to end.  ").title()
            if another_one == "No":
                should_continue = False
            else:
                record = df[df.state == another_one]
                var_x = record.x.values
                var_y = record.y.values
                print(f"{another_one}'s x: {var_x}, y: {var_y}")

get_axis()
