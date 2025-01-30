import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241220.csv")
unique_squirrels = set(data["Primary Fur Color"])
print(unique_squirrels)


squirrel_counts = []
for fur_color in unique_squirrels:
    grey_squirrels = data[data["Primary Fur Color"] == fur_color]
    squirrel_counts.append(len(grey_squirrels))
    # print(len(grey_squirrels))

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [squirrel_counts[0], squirrel_counts[1], squirrel_counts[2]]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")