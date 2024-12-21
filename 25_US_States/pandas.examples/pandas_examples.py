import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# data_json = data.to_json()
# print(data_json)
#
# temp_list = data["temp"].to_list()
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].median())
# print(data["temp"].max())
#
# print(data.condition)

# Get Data in Row
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp_F = monday.temp[0] * 9/5 + 32
print(monday_temp_F)

# Create a data frame from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")