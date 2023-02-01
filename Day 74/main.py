# --- .py translation of Jupyter Notebook/Day 74

# --- INTRODUCTION ---

# Google Trends gives us an estimate of search volume. Let's explore if
# search popularity relates to other kinds of data. Perhaps there are
# patterns in Google's search volume and the price of Bitcoin or a hot stock
# like Tesla. Perhaps search volume for the term "Unemployment Benefits" can
# tell us something about the actual unemployment rate?

# --- IMPORT STATEMENTS ---

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters

# --- READING DATA ---

df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')

df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')

df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')

# --- DATA EXPLORATION ---

# TESLA:
#   What are the shapes of the dataframes?
#   How many rows and columns?
#   What are the column names?
#   Complete the f-string to show the largest/smallest number in the search
#   data column.
#   Try the .describe() function to see some useful descriptive statistics.
#   What is the periodicity of the time series data (daily, weekly, monthly?)
#   What does a value of 100 in the Google Trend search popularity actually
#   mean?

print(df_tesla.shape)
df_tesla.head()

print(
    f'Largest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.max()}'
)
print(
    f'Smallest value for Tesla in Web Search: {df_tesla.TSLA_WEB_SEARCH.min()}'
)

df_tesla.describe()

# UNEMPLOYMENT DATA

print(df_unemployment.shape)
df_unemployment.head()

print(
    f'Largest value for "Unemployment Benefits" in Web Search: '
    f'{df_unemployment.UE_BENEFITS_WEB_SEARCH.max()}'
)

# BITCOIN DATA

print(df_btc_price.shape)
df_btc_price.head()

print(df_btc_search.shape)
df_btc_search.head()

print(
    f'Largest BTC News Search: {df_btc_search.BTC_NEWS_SEARCH.max()}'
)

# --- CHECK FOR MISSING VALUES ---

# Are there any missing values in any of the dataframes? If so,
# which rows/columns have missing values? How many missing values are there?

print(
    f'Missing values for Tesla?: {df_tesla.isna().values.any()}'
)
print(
    f'Missing values for U/E?: {df_unemployment.isna().values.any()}'
)
print(
    f'Missing values for BTC Search?: {df_btc_search.isna().values.any()}'
)
print(
    f'Missing values for BTC Price?: {df_btc_price.isna().values.any()}'
)
print(
    f'Number of missing values: {df_btc_price.isna().values.sum()}'
)
print(df_btc_price[df_btc_price.CLOSE.isna()])

# Remove any missing values that are found.

df_btc_price.dropna(inplace=True)

# --- CONVERT STRINGS TO DATETIME OBJECTS ---

# Check the data type of the entries in the DataFrame MONTH or DATE columns.
# Convert any strings into DataFrame objects. Do this for all 4 of the
# DataFrames. Double-check if your type conversion was successful.

print(type(df_tesla.MONTH[0]))

df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)

print(df_tesla.MONTH.head())

# --- CONVERTING FROM DAILY TO MONTHLY DATA ---

df_btc_monthly = df_btc_price.resample('M', on='DATE').last()

print(df_btc_monthly.shape)
df_btc_monthly.head()

# --- DATA VISUALIZATIONS ---

# --- NOTEBOOK FORMATTING & STYLE HELPERS ---

# Create locators for ticks on the time axis.

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

# Register data converters to avoid warning messages.

register_matplotlib_converters()

# --- TESLA STOCK PRICE VS. SEARCH VOLUME ---

# Plot the Tesla stock price against the Tesla search volume using a line
# chart and two different axes. Label one axis "TSLA Stock Price" and the
# other axis "Search Trend".

ax1 = plt.gca()  # Get current axis
ax2 = ax1.twinx()

ax1.set_ylabel('TSLA Stock Price')
ax2.set_ylabel('Search Trend')

ax1.plot(
    df_tesla.MONTH,
    df_tesla.TSLA_USD_CLOSE,
)
ax2.plot(
    df_tesla.MONTH,
    df_tesla.TLSA_WEB_SEARCH,
)

plt.show()

# Add colors to style the chart. This will help differentiate the two lines
# and the axis labels. Try using one of the blue colors for the search volume
# and a HEX code for a red color for the stock price.

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel(
    'TSLA Stock Price',
    color='#E6232E',  # Use a HEX Code
)
ax2.set_ylabel(
    'Search Trend',
    color='skyblue',  # Use a named color
)

ax1.plot(
    df_tesla.MONTH,
    df_tesla.TSLA_USD_CLOSE,
    color='#E6232E',
)
ax2.plot(
    df_tesla.MONTH,
    df_tesla.TSLA_WEB_SEARCH,
    color='skyblue',
)

plt.show()

# Make the chart larger & easier to read:
#   Increase the figure size.
#   Increase the font sizes for the labels & the ticks on the x-axis to 14.
#   Rotate the text on th x-axis by 45 degrees.
#   Make the lines on the chart thicker.
#   Add a title that reads "Tesla Web Search vs. Price".
#   Change the DPI of the chart.
#   Set min/max values for the y- and x-axis.
#   Use plt.show() to display the chart below the cell instead of relying on
#   the automatic notebook output.

plt.figure(
    figsize=(14, 8),  # Increase size
    dpi=120,          # Increase resolution
)
plt.title(
    'Tesla Web Search vs. Price',
    fontsize=18,
)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel(
    'TSLA Stock Price',
    color='#E6232E',
    fontsize=14,  # Increase font size
)
ax2.set_ylabel(
    'Search Trend',
    color='skyblue',
    fontsize=14,  # Increase font size
)

ax1.plot(
    df_tesla.MONTH,
    df_tesla.TSLA_USD_CLOSE,
    color='#E6232E',
    linewidth=3,  # Increase line width
)
ax2.plot(
    df_tesla.MONTH,
    df_tesla.TSLA_WEB_SEARCH,
    color='skyblue',
    linewidth=3,  # Increase line width
)

plt.show()

# Increase the size & rotate the labels on the x-axis.

plt.xticks(
    fontsize=14,
    rotation=45,
)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel(
    'TSLA Stock Price',
    color='#E6232E',
    fontsize=14,
)
ax2.set_ylabel(
    'Search Trend',
    color='skyblue',
    fontsize=14,
)

# Set the min/max values on the axes.

ax1.set_ylim([0, 600])
ax2.set_xlim([
    df_tesla.MONTH.min(),
    df_tesla.MONTH.max(),
])

plt.show()

# Add tick formatting for dates on the x-axis:

plt.figure(
    figsize=(14, 8),
    dpi=120,
)
plt.title(
    'Tesla Web Search vs. Price',
    fontsize=18,
)
plt.xticks(
    fontsize=14,
    rotation=45
)

ax1 = plt.gca()
ax2 = ax1.twinx()

# Format the ticks.

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylabel(
    'TSLA Stock Price',
    color='#E6232E',
    fontsize=14,
)
ax2.set_ylabel(
    'Search Trend',
    color='skyblue',
    fontsize=14,
)

ax1.set_ylim([0, 600])
ax1.set_xlim([
    df_tesla.MONTH.min(),
    df_tesla.MONTH.max(),
])

ax1.plot(
    df_tesla.MONTH,
    df_tesla.TSLA_USD_CLOSE,
    color='#E6232E',
    linewidth=3,
)
ax2.plot(
    df_tesla.MONTH,
    df_tesla.TSLA_WEB_SEARCH,
    color='skyblue',
    linewidth=3,
)

plt.show()

# --- BITCOIN PRICE VS SEARCH VOLUME ---

# Create a similar chart as above for Bitcoin prices vs. search volumes.

plt.figure(
    figsize=(14, 8),
    dpi=120,
)
plt.title(
    'Bitcoin News Search vs. Resampled Price',
    fontsize=18,
)
plt.xticks(
    fontsize=14,
    rotation=45,
)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel(
    'BTC Price',
    color='#F08F2E',
    fontsize=14,
)
ax2.set_ylabel(
    'Search Trend',
    color='skyblue',
    fontsize=14,
)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(
    bottom=0,
    top=15000,
)
ax1.set_xlim([
    df_btc_monthly.index.min(),
    df_btc_monthly.index.max(),
])

# Experiment with the linestyle and markers.

ax1.plot(
    df_btc_monthly.index,
    df_btc_monthly.CLOSE,
    color='#F08F2E',
    linewidth=3,
    linestyle='--',
)
ax2.plot(
    df_btc_monthly.index,
    df_btc_search.BTC_NEWS_SEARCH,
    color='skyblue',
    linewidth=3,
    marker='o',
)

plt.show()

# UNEMPLOYMENT BENEFITS SEARCH VS. ACTUAL UNEMPLOYMENT RATES IN THE U.S.

# Plot the search for "unemployment benefits" against the unemployment rate.
# Change the title to: Monthly Search of "Unemployment Benefits" in the U.S.
# vs. the U/E Rate.
# Change the y-axis label to: FRED U/E Rate.
# Change the axis limits.
# Add a grey grid to the chart to better see the years and the U/E rate
# values. Use dashes for the line style.
# Can you discern any seasonality in the searches? Is there a pattern?

plt.figure(
    figsize=(14, 8),
    dpi=120,
)
plt.title(
    'Monthly Search of "Unemployment Benefits" in the U.S. vs. the U/E Rate',
    fontsize=18,
)
plt.yticks(
    fontsize=14,
)
plt.xticks(
    fontsize=14,
    rotation=45,
)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel(
    'FRED U/E Rate',
    color='purple',
    fontsize=14,
)
ax2.set_ylabel(
    'Search Trend',
    color='skyblue',
    fontsize=14,
)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(
    bottom=3,
    top=10.5,
)
ax1.set_xlim([
    df_unemployment.MONTH.min(),
    df_unemployment.MONTH.max(),
])

# Show the grid lines as dark-grey lines.

ax1.grid(
    color='grey',
    linestyle='--',
)

# Change the dataset used.

ax1.plot(
    df_unemployment.MONTH,
    df_unemployment.UNRATE,
    color='purple',
    linewidth=3,
    linestyle='--',
)
ax2.plot(
    df_unemployment.MONTH,
    df_unemployment.UE_BENEFITS_WEB_SEARCH,
    color='skyblue',
    linewidth=3,
)

plt.show()

# Calculate the 3-month rolling average for the web searches. Plot the
# 3-month or the 6-month rolling average search data against the actual
# unemployment.

plt.figure(
    figsize=(14, 8),
    dpi=120,
)
plt.title(
    'Rolling Monthly US "Unemployment Benefits" Web Searches vs. UNRATE',
    fontsize=18,
)
plt.yticks(
    fontsize=14,
)
plt.xticks(
    fontsize=14,
    rotation=45,
)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylabel(
    'FRED U/E Rate',
    color='purple',
    fontsize=16,
)
ax2.set_ylabel(
    'Search Trend',
    color='skyblue',
    fontsize=16,
)

ax1.set_ylim(
    bottom=3,
    top=10.5,
)
ax1.set_xlim(
    df_unemployment.MONTH[0],
    df_unemployment.MONTH.max(),
)

# Calculate the average over a 6-month window:

roll_df = df_unemployment[
    [
        'UE_BENEFITS_WEB_SEARCH',
        'UNRATE',
    ]
].rolling(window=6).mean()

ax1.plot(
    df_unemployment.MONTH,
    roll_df.UNRATE,
    color='purple',
    linewidth=3,
    linestyle='-.',
)
ax2.plot(
    df_unemployment.MONTH,
    roll_df.UE_BENEFITS_WEB_SEARCH,
    color='skyblue',
    linewidth=3,
)

plt.show()

# --- INCLUDING 2020 IN UNEMPLOYMENT BENEFITS ---

# Read the data in the "UE Benefits Search vs. UE Rate 2004-20.csv" into a
# dataframe. Convert the 'MONTH' column to Pandas datetime objects and then
# plot the chart. What do you see?

df_ue_2020 = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')
df_ue_2020.MONTH = pd.to_datetime(df_ue_2020.MONTH)

plt.figure(
    figsize=(14, 8),
    dpi=20
)
plt.yticks(
    fontsize=14,
)
plt.xticks(
    fontsize=14,
    rotation=45,
)
plt.title(
    'Monthly US "Unemployment Benefits" Web Search vs. UNRATE incl. 2020',
    fontsize=18,
)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel(
    'FRED U/E Rate',
    color='purple',
    fontsize=16,
)
ax2.set_ylabel(
    'Search Trend',
    color='skyblue',
    fontsize=16,
)

ax1.set_xlim([
    df_ue_2020.MONTH.min(),
    df_ue_2020.MONTH.max(),
])

ax1.plot(
    df_ue_2020.MONTH,
    df_ue_2020.UNRATE,
    color='purple',
    linewidth=3,
)
ax2.plot(
    df_ue_2020.MONTH,
    df_ue_2020.UE_BENEFITS_WEB_SEARCH,
    color='skyblue',
    linewidth=3,
)

plt.show()
