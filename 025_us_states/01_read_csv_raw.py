data_list = []
with open("weather_data.csv") as data:
    contents = data.readlines()

    for line in contents:
        data_list.append(line)

print(contents)
