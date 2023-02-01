# -*- coding: utf-8 -*-

# -- Sheet --

# # Introduction
# 
# Do higher film budgets lead to more box office revenue? Let's find out if there's a relationship using the movie budgets and financial performance data that I've scraped from [the-numbers.com](https://www.the-numbers.com/movie/budgets) on **May 1st, 2018**. 
# 
# <img src=https://i.imgur.com/kq7hrEh.png>


# # Import Statements


import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from sklearn.linear_model import LinearRegression

# # Notebook Presentation


pd.options.display.float_format = '{:,.2f}'.format

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# # Read the Data


data = pd.read_csv('cost_revenue_dirty.csv')

# # Explore and Clean the Data


# **Challenge**: Answer these questions about the dataset:
# 1. How many rows and columns does the dataset contain?
# 2. Are there any NaN values present?
# 3. Are there any duplicate rows?
# 4. What are the data types of the columns?


data.shape

data.sample(5)

data.tail()

print(f'Any NaN values among the data? {data.isna().values.any()}')

print(f'Any duplicates? {data.duplicated().values.any()}')

duplicated_rows = data[data.duplicated()]
print(f'Number of duplicates: {len(duplicated_rows)}')

# Show NaN values and data types per column
data.info()

# ### Data Type Conversions


# **Challenge**: Convert the `USD_Production_Budget`, `USD_Worldwide_Gross`, and `USD_Domestic_Gross` columns to a numeric format by removing `$` signs and `,`. 
# <br>
# <br>
# Note that *domestic* in this context refers to the United States.


chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget', 
                    'USD_Worldwide_Gross',
                    'USD_Domestic_Gross']

for col in columns_to_clean:
    for char in chars_to_remove:
        # Replace each character with an empty string
        data[col] = data[col].astype(str).str.replace(char, "")
    # Convert column to a numeric data type
    data[col] = pd.to_numeric(data[col])

data.head()

# **Challenge**: Convert the `Release_Date` column to a Pandas Datetime type. 


data.Release_Date = pd.to_datetime(data.Release_Date)
data.head()

data.info()

# ### Descriptive Statistics


# **Challenge**: 
# 
# 1. What is the average production budget of the films in the data set?
# 2. What is the average worldwide gross revenue of films?
# 3. What were the minimums for worldwide and domestic revenue?
# 4. Are the bottom 25% of films actually profitable or do they lose money?
# 5. What are the highest production budget and highest worldwide gross revenue of any film?
# 6. How much revenue did the lowest and highest budget films make?


data.describe()

data[data.USD_Production_Budget == 1100.00]

data[data.USD_Production_Budget == 425000000.00]

# # Investigating the Zero Revenue Films


# **Challenge** How many films grossed $0 domestically (i.e., in the United States)? What were the highest budget films that grossed nothing?


zero_domestic = data[data.USD_Domestic_Gross == 0]
print(f'Number of films that grossed $0 domestically {len(zero_domestic)}')
zero_domestic.sort_values('USD_Production_Budget', ascending=False)

# **Challenge**: How many films grossed $0 worldwide? What are the highest budget films that had no revenue internationally?


zero_worldwide = data[data.USD_Worldwide_Gross == 0]
print(f'Number of films that grossed $0 worldwide {len(zero_worldwide)}')
zero_worldwide.sort_values('USD_Production_Budget', ascending=False)

# ### Filtering on Multiple Conditions


international_releases = data.loc[(data.USD_Domestic_Gross == 0) & 
                                  (data.USD_Worldwide_Gross != 0)]
print(f'Number of international releases: {len(international_releases)}')
international_releases.head()

# **Challenge**: Use the [`.query()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) to accomplish the same thing. Create a subset for international releases that had some worldwide gross revenue, but made zero revenue in the United States. 
# 
# Hint: This time you'll have to use the `and` keyword.


international_releases = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
print(f'Number of international releases: {len(international_releases)}')
international_releases.tail()

# ### Unreleased Films
# 
# **Challenge**:
# * Identify which films were not released yet as of the time of data collection (May 1st, 2018).
# * How many films are included in the dataset that have not yet had a chance to be screened in the box office? 
# * Create another DataFrame called data_clean that does not include these films. 


# Date of Data Collection
scrape_date = pd.Timestamp('2018-5-1')

future_releases = data[data.Release_Date >= scrape_date]
print(f'Number of unreleased movies: {len(future_releases)}')
future_releases

# exclude future releases
data_clean = data.drop(future_releases.index)

# difference is 7 rows
data.shape[0] - data_clean.shape[0]

# ### Films that Lost Money
# 
# **Challenge**: 
# What is the percentage of films where the production costs exceeded the worldwide gross revenue? 


money_losing = data_clean.loc[data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]
len(money_losing)/len(data_clean)

money_losing = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
money_losing.shape[0]/data_clean.shape[0]

# # Seaborn for Data Viz: Bubble Charts


plt.figure(figsize=(8,4), dpi=200)

ax = sns.scatterplot(data=data_clean,
                     x='USD_Production_Budget', 
                     y='USD_Worldwide_Gross')

ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions')

plt.show()

plt.figure(figsize=(8,4), dpi=200)
ax = sns.scatterplot(data=data_clean,
                     x='USD_Production_Budget', 
                     y='USD_Worldwide_Gross',
                     hue='USD_Worldwide_Gross', # change colour
                     size='USD_Worldwide_Gross',) # change size of dot

ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions',)

plt.show()

plt.figure(figsize=(8,4), dpi=200)

# set styling on a single chart
with sns.axes_style('darkgrid'):
  ax = sns.scatterplot(data=data_clean,
                       x='USD_Production_Budget', 
                       y='USD_Worldwide_Gross',
                       hue='USD_Worldwide_Gross',
                       size='USD_Worldwide_Gross')

  ax.set(ylim=(0, 3000000000),
        xlim=(0, 450000000),
        ylabel='Revenue in $ billions',
        xlabel='Budget in $100 millions')

# ### Plotting Movie Releases over Time
# 
# **Challenge**: Try to create the following Bubble Chart:
# 
# <img src=https://i.imgur.com/8fUn9T6.png>


plt.figure(figsize=(8,4), dpi=200)

with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=data_clean, 
                    x='Release_Date', 
                    y='USD_Production_Budget',
                    hue='USD_Worldwide_Gross',
                    size='USD_Worldwide_Gross',)

    ax.set(ylim=(0, 450000000),
           xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
           xlabel='Year',
           ylabel='Budget in $100 millions')

# # Converting Years to Decades Trick
# 
# **Challenge**: Create a column in `data_clean` that has the decade of the release. 
# 
# <img src=https://i.imgur.com/0VEfagw.png width=650> 
# 
# Here's how: 
# 1. Create a [`DatetimeIndex` object](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.html) from the Release_Date column. 
# 2. Grab all the years from the `DatetimeIndex` object using the `.year` property.
# <img src=https://i.imgur.com/5m06Ach.png width=650>
# 3. Use floor division `//` to convert the year data to the decades of the films.
# 4. Add the decades as a `Decade` column to the `data_clean` DataFrame.


dt_index = pd.DatetimeIndex(data_clean.Release_Date)
years = dt_index.year

# How to convert the year 1999 to the 90s decade
1999//10

199*10

decades = years//10*10
data_clean['Decade'] = decades

# ### Separate the "old" (before 1969) and "New" (1970s onwards) Films
# 
# **Challenge**: Create two new DataFrames: `old_films` and `new_films`
# * `old_films` should include all the films before 1969 (up to and including 1969)
# * `new_films` should include all the films from 1970 onwards
# * How many films were released prior to 1970?
# * What was the most expensive film made prior to 1970?


old_films = data_clean[data_clean.Decade <= 1960]
new_films = data_clean[data_clean.Decade > 1960]

old_films.describe()

old_films.sort_values('USD_Production_Budget', ascending=False).head()

# # Seaborn Regression Plots


sns.regplot(data=old_films, 
            x='USD_Production_Budget',
            y='USD_Worldwide_Gross')

plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("whitegrid"):
  sns.regplot(data=old_films, 
            x='USD_Production_Budget', 
            y='USD_Worldwide_Gross',
            scatter_kws = {'alpha': 0.4},
            line_kws = {'color': 'black'})

# **Challenge**: Use Seaborn's `.regplot()` to show the scatter plot and linear regression line against the `new_films`. 
# <br>
# <br>
# Style the chart
# 
# * Put the chart on a `'darkgrid'`.
# * Set limits on the axes so that they don't show negative values.
# * Label the axes on the plot "Revenue in \$ billions" and "Budget in \$ millions".
# * Provide HEX colour codes for the plot and the regression line. Make the dots dark blue (#2f4b7c) and the line orange (#ff7c43).
# 
# Interpret the chart
# 
# * Do our data points for the new films align better or worse with the linear regression than for our older films?
# * Roughly how much would a film with a budget of $150 million make according to the regression line?


plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style('darkgrid'):
  ax = sns.regplot(data=new_films,
                   x='USD_Production_Budget',
                   y='USD_Worldwide_Gross',
                   color='#2f4b7c',
                   scatter_kws = {'alpha': 0.3},
                   line_kws = {'color': '#ff7c43'})
  
  ax.set(ylim=(0, 3000000000),
         xlim=(0, 450000000),
         ylabel='Revenue in $ billions',
         xlabel='Budget in $100 millions')

# # Run Your Own Regression with scikit-learn
# 
# Our Linear Model:
# 
# $$ REV \hat ENUE = \theta _0 + \theta _1 BUDGET$$


# Create regression object
regression = LinearRegression()

# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])

# Response Variable or Target
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross'])

# Find the best-fit line
regression.fit(X, y)

# Theta zero
regression.intercept_

# Theta one
regression.coef_

# R-squared
regression.score(X, y)

# **Challenge**: Run a linear regression for the `old_films`. Calculate the intercept, slope and r-squared. How much of the variance in movie revenue does the linear model explain in this case?


X = pd.DataFrame(old_films, columns=['USD_Production_Budget'])
y = pd.DataFrame(old_films, columns=['USD_Worldwide_Gross'])
regression.fit(X, y)
print(f'The slope coefficient is: {regression.coef_[0]}')
print(f'The intercept is: {regression.intercept_[0]}')
print(f'The r-squared is: {regression.score(X, y)}')

# # Use Your Model to Make a Prediction
# 
# We just estimated the slope and intercept! Remember that our Linear Model has the following form:
# 
# $$ REV \hat ENUE = \theta _0 + \theta _1 BUDGET$$
# 
# **Challenge**:  How much global revenue does our model estimate for a film with a budget of $350 million? 


22821538 + 1.64771314 * 350000000

budget = 350000000
revenue_estimate = regression.intercept_[0] + regression.coef_[0,0]*budget
revenue_estimate = round(revenue_estimate, -6)
print(f'The estimated revenue for a $350 film is around ${revenue_estimate:.10}.')

