import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)
# print(df.head())
# print(df.tail())
# print(df.shape)

# m_nan_count = df["DATE"].isna().sum()
# print(m_nan_count)
#
# m_nan_count = df["TAG"].isna().sum()
# print(m_nan_count)
#
# m_nan_count = df["POSTS"].isna().sum()
# print(m_nan_count)

# print(df.count())

# how many posts each programming language had since the creation of Stack Overflow
# print(df.groupby("TAG").sum())
# months of entries exist per programming language
# print(df.groupby("TAG").count())

# Selecting an Individual Cell
# print(df["DATE"][1])
# print(df.DATE[1])

# print(pd.to_datetime(df.DATE[1]))
# print(type(pd.to_datetime(df.DATE[1])))

# Convert Entire Column
df.DATE = pd.to_datetime(df.DATE)

# print(df.head())

test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
# print(test_df)

pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
# print(pivoted_df)

reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
# print(reshaped_df)
# print(reshaped_df.shape)
reshaped_df.fillna(0, inplace=True)

# print(reshaped_df.head())
# print(reshaped_df.tail())

# print(reshaped_df.columns)
# print(reshaped_df.count())

check_nan = reshaped_df.isna().values.any()
# print(check_nan)

# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=7).mean()

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
plt.title("Programming Languages Popularity According to \"Stack Overflow\" Comments")

# plt.plot(reshaped_df.index, reshaped_df.java)
# plt.plot(reshaped_df.index, reshaped_df.python)

# plot all languages using for loop
for column in roll_df.columns:
# for column in roll_df.columns[6::4]:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=reshaped_df[column].name)

plt.legend(fontsize=16)

plt.show(block=True)
