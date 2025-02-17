import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_tesla = pd.read_csv('data/TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('data/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('data/Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-19.csv')

data_frames = []
data_frames.extend([df_tesla, df_btc_search, df_btc_price, df_unemployment])

# [print(f"{df.shape}\n{df.columns}\n{df.describe()}\n\n") for df in data_frames]

# print(f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}')
# print(f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}')

# print(f'Smallest value for "Unemployment Benefits" '
#       f'in Web Search: {df_unemployment.UE_BENEFITS_WEB_SEARCH.min()}')
# print(f'Largest value for "Unemployment Benefits" '
#       f'in Web Search: {df_unemployment.UE_BENEFITS_WEB_SEARCH.max()}')

# print(f'Largest BTC News Search: {df_btc_search.BTC_NEWS_SEARCH.max()}')

# [print(f"{df.isna().values.any()}. DF index: {i}") for i, df in enumerate(data_frames)]

# print(f'Missing values? for Tesla?: {df_tesla.isna().values.any()}')
# print(f'Missing values? for U/E?: {df_unemployment.isna().values.any()}')
# print(f'Missing values? for BTC Search?: {df_btc_search.isna().values.any()}')
# print(f'Missing values? for BTC price?: {df_btc_price.isna().values.any()}')

# print(f'Number of missing values: {df_btc_price.isna().values.sum()}')
# print(df_btc_price[df_btc_price.CLOSE.isna()])

df_btc_price.dropna(inplace=True)
# print(f'Number of missing values: {df_btc_price.isna().values.sum()}')
# print(df_btc_price[df_btc_price.CLOSE.isna()])

# print(type(df_tesla.MONTH[0]))
# print(df_tesla.MONTH.head())

df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)

# print(df_tesla.MONTH.head())

df_btc_monthly = df_btc_price.resample('ME', on='DATE').last()
# df_btc_monthly = df_btc_price.resample('M', on='DATE').mean()
# print(df_btc_monthly.shape)
# print(df_btc_search.shape)

# increases size and resolution
# plt.figure(figsize=(14, 8), dpi=120)
# plt.title('Tesla Web Search vs Price', fontsize=18)

# ax1 = plt.gca()  # get current axis
# ax2 = ax1.twinx()

# Also, increase fontsize and linewidth for larger charts
# ax1.set_ylabel("TESLA Stock Price", color="#E6232E", fontsize=14)  # HEX code
# ax2.set_ylabel("Search Trend", color="skyblue", fontsize=14)  # named colour

# ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color="#E6232E", linewidth=3)
# ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color="skyblue", linewidth=3)

# https://matplotlib.org/3.1.1/gallery/color/named_colors.html
# https://htmlcolorcodes.com/color-picker/

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter("%Y")

# format the ticks
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)

# Displays chart explicitly
# plt.show()

# plt.figure(figsize=(14, 8), dpi=120)
#
# plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
# plt.xticks(fontsize=14, rotation=45)
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
#
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
# ax1.set_ylim(bottom=0, top=15000)
# ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])
#
# # Experiment with the linestyle and markers
# ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE,
#          color='#F08F2E', linewidth=3, linestyle='--')
# ax2.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH,
#          color='skyblue', linewidth=3, marker='o')
#
# plt.show()

# plt.figure(figsize=(14, 8), dpi=120)
# plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
# plt.yticks(fontsize=14)
# plt.xticks(fontsize=14, rotation=45)
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)
#
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
# roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
#
# ax1.set_ylim(bottom=3, top=10.5)
# ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])
#
# # Show the grid lines as dark grey lines
# ax1.grid(color='grey', linestyle='--')
#
# # Change the dataset used
# ax1.plot(df_unemployment.MONTH, roll_df.UNRATE, color='purple', linewidth=3, linestyle='--')
# ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, color='skyblue', linewidth=3)
#
# plt.show()

df_ue_2020 = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-20.csv')
df_ue_2020.MONTH = pd.to_datetime(df_ue_2020.MONTH)

plt.figure(figsize=(14, 8), dpi=120)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
plt.title('Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)

ax1.set_xlim([df_ue_2020.MONTH.min(), df_ue_2020.MONTH.max()])

ax1.plot(df_ue_2020.MONTH, df_ue_2020.UNRATE, 'purple', linewidth=3)
ax2.plot(df_ue_2020.MONTH, df_ue_2020.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=3)

plt.show()
