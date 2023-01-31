import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")

print(df.head())
print("==========")

print(df.shape)
print("==========")

print(df.columns)
print("==========")

print(df.isna())
print("==========")

print(df.tail())
print("==========")

clean_df = df.dropna()
print(clean_df.tail())
print("==========")

print(clean_df['Starting Median Salary'].max())
print("==========")

print(clean_df['Starting Median Salary'].idxmax())
print("==========")

print(clean_df['Starting Median Salary'][43])
print("==========")

print(clean_df['Undergraduate Major'].loc[43])
print("==========")

print(clean_df['Undergraduate Major'][43])
print("==========")

print(clean_df.loc[43])
print("==========")

print(clean_df['Mid-Career Median Salary'].max())
print(
    f"Index for the max mid career salary: "
    f"{clean_df['Mid-Career Median Salary'].idxmax()}")
print(clean_df['Undergraduate Major'][8])
print("==========")

print(clean_df['Starting Median Salary'].min())
print(clean_df['Undergraduate Major'].loc[clean_df['Starting Median '
                                                   'Salary'].idxmin()])
print("==========")

print(clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()])
print("==========")

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df[
    'Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
print(clean_df.head())
print("==========")

low_risk = clean_df.sort_values('Spread')
print(low_risk[['Undergraduate Major', 'Spread']].head())
print("==========")

highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary',
                                         ascending=False)
print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile '
                                                'Salary']].head())
print("==========")

highest_spread = clean_df.sort_values('Spread', ascending=False)
print(highest_spread[['Undergraduate Major', 'Spread']].head())
print("==========")

highest_spread = clean_df.sort_values('Mid-Career Median Salary',
                                      ascending=False)
print(highest_spread[['Undergraduate Major', 'Mid-Career Median '
                                             'Salary']].head())
print("==========")

print(clean_df.groupby('Group').count())
print("==========")

pd.options.display.float_format = '{:,.2f}'.format
print(clean_df.groupby('Group').mean())
print("==========")
