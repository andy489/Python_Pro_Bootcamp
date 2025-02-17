import pandas as pd
import matplotlib.pyplot as plt

colors = pd.read_csv("data/colors.csv")

# num_colors = colors.groupby("name").count()
# print(num_colors.shape[0])
# print(colors["name"].nunique())


# num_transparent = colors.groupby(["is_trans"]).apply(len, include_groups=False)
# print(num_transparent)
# print(colors.groupby(["is_trans"]).count())
# print(colors.is_trans.value_counts())

sets = pd.read_csv("data/sets.csv")
# print(sets.head())
# print(sets.tail())

first_lego_index = sets["year"].idxmin()
first_lego = sets.loc[first_lego_index][["year", "name"]]
first_lego_year = sets.loc[first_lego_index]["year"]
# print(first_lego_year)
# print(sets.sort_values("year").head())

# print(sets.groupby("year").nunique())
# print(sets[sets["year"] == first_lego_year])

largest_num_parts_index = sets["num_parts"].idxmax()
largest_num_parts = sets.loc[largest_num_parts_index]
# print(largest_num_parts)
# print(sets.sort_values("num_parts", ascending=False).head())

sets_by_year = sets.groupby("year").count()
# print(sets_by_year["set_num"].head())
# print(sets_by_year["set_num"].tail())

# plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
# plt.show()

themes_by_year = sets.groupby("year").agg({"theme_id": pd.Series.nunique})
# print(themes_per_year)

themes_by_year.rename(columns={"theme_id": "nr_themes"}, inplace=True)
# print(themes_by_year.head())
# print(themes_by_year.tail())

# plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
# plt.show()

# ax1 = plt.gca()  # get current axes
# ax2 = ax1.twinx()
# ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color="g")
# ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color="b")

# ax1.set_xlabel("Year")
# ax1.set_ylabel("Number of Sets", color="green")
# ax2.set_ylabel("Number of Themes", color="blue")
# plt.show()

parts_per_set = sets.groupby("year").agg({"num_parts": pd.Series.mean}).round(2)
parts_per_set.rename(columns={"num_parts": "avg_parts"}, inplace=True)
# print(parts_per_set.head())
# print(parts_per_set.tail())

# plt.scatter(parts_per_set.index[:-2], parts_per_set.avg_parts[:-2])
# plt.show()

themes = pd.read_csv("data/themes.csv")
# print(themes.head())
# print(themes.tail())
# print(themes[themes["name"] == "Star Wars"])
# print(sets[sets.theme_id == 18])
# print(sets[sets.theme_id == 209])

set_theme_count = sets["theme_id"].value_counts()
# print(set_theme_count[:5])

set_theme_count = pd.DataFrame({"id": set_theme_count.index,
                                "set_count": set_theme_count.values})

# print(set_theme_count.head())

merged_df = pd.merge(set_theme_count, themes, on="id")
# print(merged_df[:3])

plt.figure(figsize=(14, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.subplots_adjust(bottom=0.3)
plt.show()
