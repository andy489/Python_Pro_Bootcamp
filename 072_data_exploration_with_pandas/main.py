import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")
# print(df.head())

# print(df.shape)
# print(df.columns)
# print(df.isna())
# print(df.tail())
# https://www.w3schools.com/python/pandas/ref_df_dropna.asp#:~:text=Definition%20and%20Usage,in%20the%20original%20DataFrame%20instead.
clean_df = df.dropna(axis="index", how="any")
# print(clean_df.tail())

UNDERGRADUATE_MAJOR = "Undergraduate Major"
STARTING_MEDIAN_SALARY = "Starting Median Salary"
MID_CAREER_MEDIAN_SALARY = "Mid-Career Median Salary"
MID_CAREER_10TH_PERCENTILE_SALARY = "Mid-Career 10th Percentile Salary"
MID_CAREER_90TH_PERCENTILE_SALARY = "Mid-Career 90th Percentile Salary"
GROUP = "Group"

"""
The Highest Mid-Career Salary
"""
ind_1 = clean_df[MID_CAREER_MEDIAN_SALARY].idxmax()
# print(clean_df[MID_CAREER_MEDIAN_SALARY].max())
# print(f"Index for the max mid career salary: {ind_1}")
# print(clean_df[UNDERGRADUATE_MAJOR].loc[ind_1])

"""
The Lowest Starting and Mid-Career Salary
"""
ind_2 = clean_df[STARTING_MEDIAN_SALARY].idxmin()
# print(clean_df[STARTING_MEDIAN_SALARY].min())
# print(clean_df[UNDERGRADUATE_MAJOR].loc[ind_2])

"""
Which college major has the lowest starting salary and how much do graduates earn after university?
"""
ind_3 = clean_df[MID_CAREER_MEDIAN_SALARY].idxmin()
# print(clean_df[MID_CAREER_MEDIAN_SALARY].min())
# print(clean_df.loc[ind_3])

"""
Which college major has the lowest mid-career salary and how much can people expect to earn with this degree? 
"""
ind_4 = clean_df[MID_CAREER_MEDIAN_SALARY].idxmin()
target_row = clean_df.loc[ind_4]
# print(target_row[1:len(target_row) - 1].mean())

"""
Sorting Values & Adding Columns: Majors with the Most Potential vs Lowest Risk
"""
row_1 = clean_df[MID_CAREER_90TH_PERCENTILE_SALARY]
row_2 = clean_df[MID_CAREER_10TH_PERCENTILE_SALARY]
# spread_col = row_1.subtract(row_2)
spread_col = row_1 - row_2
# print(spread_col)
clean_df.insert(1, 'Spread', spread_col)
# print(clean_df.head())

"""
Sorting by the Lowest Spread
"""
low_risk = clean_df.sort_values('Spread')
res_1 = low_risk[[UNDERGRADUATE_MAJOR, 'Spread']].head()
# print(res_1)

"""
Majors with the Highest Potential
"""
res_2 = ((clean_df[[UNDERGRADUATE_MAJOR, MID_CAREER_90TH_PERCENTILE_SALARY]]
          .sort_values(by=MID_CAREER_90TH_PERCENTILE_SALARY, ascending=False))
         .head())

# print(res_2)

"""
Majors with the Greatest Spread in Salaries
"""
res_3 = ((clean_df[[UNDERGRADUATE_MAJOR, "Spread"]]
          .sort_values(by="Spread", ascending=False))
         .head())

# print(res_3)
groups = clean_df.groupby(GROUP).count()
print(groups)
group_means = clean_df.drop(UNDERGRADUATE_MAJOR, axis=1).groupby(GROUP).mean()

pd.options.display.float_format = '{:,.2f}'.format

print(group_means)

# https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors