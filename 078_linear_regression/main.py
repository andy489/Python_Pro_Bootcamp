import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("cost_revenue_dirty.csv")

# print(data.shape)

# print(data.head())
# print(data.tail())

# print(data.sample())

# print(data.isna().any()) # per column
nan_values_check = data.isna().values.any()
# print(f"Any Nan values among the data? {nan_values_check}")

# print(data.duplicated().any()) # per column
duplicates_check = data.duplicated().values.any()
# print(f"Any duplicates? {duplicates_check}")

duplicated_rows = data[data.duplicated()]
# print(duplicated_rows)
# print(f"Number of duplicates: {len(duplicated_rows)}")

# print(data.info())

chars_to_remove = [",", "$"]
columns_to_clean = ["USD_Production_Budget", "USD_Worldwide_Gross", "USD_Domestic_Gross"]

for col in columns_to_clean:
    for char in chars_to_remove:
        # Replace each character with an empty string
        data[col] = data[col].astype(str).str.replace(char, "")
    # Convert column to a numeric data type
    data[col] = pd.to_numeric(data[col])

data.Release_Date = pd.to_datetime(data.Release_Date)

# print(data.info())

# print(data.describe())
min_prod_budget = data.describe(include="all").loc["min"].USD_Production_Budget
# print(data[data.USD_Production_Budget == min_prod_budget]["Movie_Title"])
# print(data[data.USD_Production_Budget == 1100.00])

max_prod_budget = data.describe(include="all").loc["max"].USD_Production_Budget
# print(data[data.USD_Production_Budget == max_prod_budget]["Movie_Title"])
# print(data[data.USD_Production_Budget == 425000000.0])

zero_domestic = data[data.USD_Domestic_Gross == 0]
# print(f'Number of films that grossed $0 domestically {len(zero_domestic)}')
ascending_domestic = zero_domestic.sort_values('USD_Production_Budget', ascending=False)
# print(ascending_domestic)

zero_worldwide = data[data.USD_Worldwide_Gross == 0]
# print(f'Number of films that grossed $0 worldwide {len(zero_worldwide)}')
zero_worldwide.sort_values('USD_Production_Budget', ascending=False)

international_releases1 = data.loc[(data.USD_Domestic_Gross == 0) &
                                   (data.USD_Worldwide_Gross != 0)]
# print(international_releases1)

international_releases2 = data.query("USD_Worldwide_Gross > 0 and USD_Domestic_Gross == 0")
# print(f'Number of international releases: {len(international_releases2)}')
# print(international_releases2.tail())

# Date of Data Collection
scrape_date = pd.Timestamp("2018-5-1")

future_releases = data[data.Release_Date >= scrape_date]
# print(f"Number of unreleased movies: {len(future_releases)}")
# print(future_releases)

data_clean = data.drop(future_releases.index)

money_losing1 = data_clean.loc[data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]
# print(len(money_losing1)/len(data_clean))

money_losing2 = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
# print(round(money_losing2.shape[0] / data_clean.shape[0], 4))

# plt.figure(figsize=(8, 4), dpi=200)
# ax = sns.scatterplot(data=data_clean,
#                      x='USD_Production_Budget',
#                      y='USD_Worldwide_Gross')
#
# ax.set(ylim=(0, 3_000_000_000),
#        xlim=(0, 450_000_000),
#        ylabel='Revenue in $ billions',
#        xlabel='Budget in $100 millions')

# plt.figure(figsize=(8, 4), dpi=200)
# ax = sns.scatterplot(data=data_clean,
#                      x='USD_Production_Budget',
#                      y='USD_Worldwide_Gross',
#                      hue='USD_Worldwide_Gross', # colour
#                      size='USD_Worldwide_Gross',) # dot size
#
# ax.set(ylim=(0, 3_000_000_000),
#        xlim=(0, 450_000_000),
#        ylabel='Revenue in $ billions',
#        xlabel='Budget in $100 millions')

# plt.figure(figsize=(8, 4), dpi=200)
# # set styling on a single chart
# with sns.axes_style('darkgrid'): # 'whitegrid', 'dark', 'ticks', etc.
#     ax = sns.scatterplot(data=data_clean,
#                          x='USD_Production_Budget',
#                          y='USD_Worldwide_Gross',
#                          hue='USD_Worldwide_Gross',
#                          size='USD_Worldwide_Gross')
#
#     ax.set(ylim=(0, 3000000000),
#            xlim=(0, 450000000),
#            ylabel='Revenue in $ billions',
#            xlabel='Budget in $100 millions')

# plt.figure(figsize=(8, 4), dpi=200)
# # set styling on a single chart
# with sns.axes_style('darkgrid'): # 'whitegrid', 'dark', 'ticks', etc.
#     ax = sns.scatterplot(data=data_clean,
#                          x='Release_Date',
#                          y='USD_Production_Budget',
#                          hue='USD_Worldwide_Gross',
#                          size='USD_Worldwide_Gross')
#
#     ax.set(ylim=(0, 450000000),
#            xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
#            ylabel='Year',
#            xlabel='Budget in $100 millions')

dt_index = pd.DatetimeIndex(data_clean.Release_Date)
years = dt_index.year
decades = years // 10 * 10
data_clean['Decade'] = decades

# print(data_clean)

# Separate the films made before and after 1970
# The cut-off for our calculation is 1960 in the Decade column because this will still include 1969
old_films = data_clean[data_clean.Decade <= 1960]
new_films = data_clean[data_clean.Decade > 1960]

# print(old_films.describe())
# print(old_films.sort_values("USD_Production_Budget", ascending=False).head())

# plt.figure(figsize=(8, 4), dpi=200)
# # set styling on a single chart
# with sns.axes_style('darkgrid'): # 'whitegrid', 'dark', 'ticks', etc.
#     ax = sns.scatterplot(data=data_clean,
#                          x='Decade',
#                          y='USD_Production_Budget',
#                          hue='USD_Worldwide_Gross',
#                          size='USD_Worldwide_Gross')
#
#     ax.set(ylim=(0, 450000000),
#            xlim=(data_clean.Decade.min(), data_clean.Decade.max()),
#            ylabel='Year',
#            xlabel='Budget in $100 millions')

# plt.figure(figsize=(8,4), dpi=200)
# with sns.axes_style("whitegrid"):
#   sns.regplot(data=old_films,
#             x='USD_Production_Budget',
#             y='USD_Worldwide_Gross',
#             scatter_kws = {'alpha': 0.4},
#             line_kws = {'color': 'black'})

# plt.figure(figsize=(8, 4), dpi=200)
# with sns.axes_style("darkgrid"):
#     ax = sns.regplot(data=new_films,
#                      x='USD_Production_Budget',
#                      y='USD_Worldwide_Gross',
#                      color="#2f4b7c",
#                      scatter_kws={'alpha': 0.3},
#                      line_kws={'color': '#ff7c43'})
#
#     ax.set(ylim=(0, 3_000_000_000),
#            xlim=(0, 450_000_000),
#            ylabel='Revenue in $ billions',
#            xlabel='Budget in $100 millions')

regression = LinearRegression()

# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])

# Response Variable or Target
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross'])

# Find the best-fit line
# regression.fit(X, y)

# Revenue = Theta_0 + Theta_1 * Budget

# Theta zero
# print(regression.intercept_)

# Theta one
# print(regression.coef_)

# R-squared
# print(regression.score(X, y))
# We see that our r-squared comes in at around 0.558.
# This means that our model explains about 56% of the variance in movie revenue.

# Explanatory Variable(s) or Feature(s)
X_old = pd.DataFrame(old_films, columns=['USD_Production_Budget'])

# Response Variable or Target
y_old = pd.DataFrame(old_films, columns=['USD_Worldwide_Gross'])

regression_old = LinearRegression()
regression_old.fit(X_old, y_old)

# Theta zero
# print(f"The intercept is: {regression_old.intercept_[0]}")

# Theta one
# print(f"The slope coefficient is: {regression_old.coef_[0]}")

# R-squared
# print(f"The r-squared is: {regression_old.score(X_old, y_old)}")
# We see that our r-squared comes in at around 0.558.
# This means that our model explains about 56% of the variance in movie revenue.

# Find the best-fit line
regression_old.fit(X, y)

# plt.show()

target_budget = 350_000_000
revenue_estimate = regression_old.intercept_[0] + regression_old.coef_[0, 0] * target_budget
# print(revenue_estimate)
revenue_estimate = round(revenue_estimate, -6)

print(f'The estimated revenue for a $350 film is around ${revenue_estimate:,.2f}.')
