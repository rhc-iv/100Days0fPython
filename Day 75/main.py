# --- INTRODUCTION ---

# In this module, we will do a comprehensive analysis of the Android app
# market by comparing thousands of apps in the Google Play store.

# --- IMPORT STATEMENTS ---

import pandas as pd
import plotly.express as px

# Show numeric output in decimal format e.g., 2.15.

pd.options.display.float_format = '{:,.2f}'.format

# Read the dataset.

df_apps = pd.read_csv('apps.csv')

# --- DATA CLEANING ---

print(df_apps.shape)
df_apps.head()
df_apps.sample(5)

# --- DROP UNUSED COLUMNS ---

# Remove the columns called "Last_Updated" and "Android_Ver" from the
# dataframe. We will not use these columns.

df_apps.drop(
    ['Last_updated', 'Android_Ver'],
    axis=1,
    inplace=True,
)
df_apps.head()

# --- FIND & REMOVE NaN VALUES IN RATING ---

# How many rows have a NaN value in the Ratings column? Create a dataframe
# called 'df_apps_clean' that does not include these rows.

nan_rows = df_apps[df_apps.Rating.isna()]
print(nan_rows.shape)
nan_rows.head()

df_apps_clean = df_apps.dropna()
print(df_apps_clean.shape)

# --- FIND & REMOVE DUPLICATES ---

# Are there any duplicates in the data? Check for duplicates using the
# duplicated() function. How many entries can you find for the "Instagram"
# app? Use drop_duplicates() to remove any duplicates from 'df_apps_clean'.

duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
print(duplicated_rows.shape)
duplicated_rows.head()

print(df_apps_clean[df_apps_clean.App == 'Instagram'])

df_apps_clean = df_apps_clean.drop_duplicates()

print(df_apps_clean[df_apps_clean.App == 'Instagram'])

# Specify the subset for identifying duplicates.

df_apps_clean = df_apps_clean.drop_duplicates(
    subset=[
        'App',
        'Type',
        'Price',
    ]
)
print(df_apps_clean[df_apps_clean.App == 'Instagram'])
print(df_apps_clean.shape)

# --- FIND HIGHEST-RATED APPS ---

# Identify which apps are the highest-rated. What problem might you encounter
# if you rely exclusively on ratings alone to determine the quality of an app?

df_apps_clean.sort_values(
    'Rating',
    ascending=False,
).head()

# --- FIND THE 5 LARGEST APPS IN TERMS OF SIZE (MBs) ---

# What's the size in megabytes (MB) of the largest Android apps in the Google
# Play store? Based on the data, do you think there could be limits in place
# or can developers make apps as large as they please?

df_apps_clean.sort_values(
    'Size_MBs',
    ascending=False,
).head()

# --- FIND THE 5 APPS WITH THE MOST REVIEWS ---

# Which apps have the highest number of reviews? Are there any paid apps
# among the Top 50?

df_apps_clean.sort_values(
    'Reviews',
    ascending=False,
).head(50)

# --- PLOTLY PIE/DONUT CHARTS - VISUALIZE CATEGORICAL DATA: CONTENT RATINGS ---

ratings = df_apps_clean.Content_Rating.value_counts()
print(ratings)

fig = px.pie(
    labels=ratings.index,
    values=ratings.values,
)

fig.show()

fig = px.pie(
    labels=ratings.index,
    values=ratings.values,
    title='Content Rating',
    names=ratings.index,
)

fig.update_traces(
    textposition='outside',
    textinfo='percent+label',
)

fig.show()

fig = px.pie(
    labels=ratings.index,
    values=ratings.values,
    title='Content Rating',
    names=ratings.index,
    hole=0.6,  # Makes a donut chart.
)

fig.update_traces(
    textposition='inside',
    textfont_size=15,
    textinfo='percent',
)

fig.show()

# --- NUMERIC TYPE CONVERSION: EXAMINE THE NUMBER OF INSTALLS ---

# How many apps have over 1 billion installations? How many apps have just a
# single installation?  Check the datatype of the "Installs" column. Count
# the number of apps at each level of installation. Convert the number of
# installations to a numeric data type.

df_apps_clean.Installs.describe()

df_apps_clean.info()

# Installs of data type object because of the comma (,) character.

df_apps_clean[
    [
        'App',
        'Installs',
    ]
].groupby('Installs').count()

df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")

df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)

df_apps_clean[
    [
        'App',
        'Installs',
    ]
].groupby('Installs').count()

# Find the most expensive apps, filter out the junk, & calculate a ballpark
# Sales Revenue Estimate.

# Let's examine the "Price" column nore closely. Convert the "Price" column
# to numeric data. Then, investigate the Top-20 most-expensive apps in the
# dataset.

# Add a column called 'Revenue_Estimate' to the dataframe. This column should
# hold the price of the app x then number of installs. What are the Top-10
# highest-grossing paid apps according to this estimate? Out of the Top-10
# highest-grossing paid apps, how many are games?

df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)

df_apps_clean.sort_values(
    'Price',
    ascending=False,
).head(20)

# --- THE MOST EXPENSIVE APPS SUB-$250 ---

df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
df_apps_clean.sort_values(
    'Price',
    ascending=False,
).head(5)

# --- HIGHEST-GROSSING PAID APPS (BALLPARK ESTIMATE) ---

df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(
    df_apps_clean.Price
)
print(df_apps_clean.sort_values(
    'Revenue_Estimate',
    ascending=False,
)[:10])

# --- PLOTLY BAR CHARTS/SCATTER PLOTS: ANALYSING APP CATEGORIES ---

# Number of different categories.

df_apps_clean.Category.nunique()

# Number of apps per category.

top10_category = df_apps_clean.Category.value_counts()[:10]
print(top10_category)

# --- VERTICAL BAR CHART - HIGHEST COMPETITION (NUMBER OF APPS) ---

bar = px.bar(
    x=top10_category.index,  # Index = Category Name
    y=top10_category.values,
)

bar.show()

# --- HORIZONTAL BAR CHART - MOST POPULAR CATEGORIES (HIGHEST DOWNLOADS) ---

# Group apps by category & then sum the number of installations.

category_installs = df_apps_clean.groupby('Category').agg(
    {'Installs': pd.Series.sum}
)
category_installs.sort_values(
    'Installs',
    ascending=True,
    inplace=True,
)

h_bar = px.bar(
    x=category_installs.Installs,
    y=category_installs.index,
    orientation='h',
    title='Category Popularity',
)

h_bar.update_layout(
    xaxis_title='Number of Downloads',
    yaxis_title='Category',
)

h_bar.show()

# --- CATEGORY CONCENTRATION - DOWNLOADS VS. COMPETITION ---

# First, create a dataframe that has the number of apps in one column and the
# number of installs in another column. Then use the Plotly Express examples
# from the documentation alongside the scatter() API reference to create
# scatter plots.

# Count the number of apps in each category (similar to what we did above).

cat_number = df_apps_clean.groupby('Category').agg(
    {'App': pd.Series.count}
)
cat_merged_df = pd.merge(
    cat_number,
    category_installs,
    on='Category',
    how='inner',
)
print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
cat_merged_df.sort_values(
    'Installs',
    ascending=False,
)

scatter = px.scatter(
    cat_merged_df,  # Data
    x='App',  # Column Name
    y='Installs',
    title='Category Concentration',
    size='App',
    hover_name=cat_merged_df.index,
    color='Installs',
)

scatter.update_layout(
    xaxis_title='Number of Apps (Lower = More Concentrated)',
    yaxis_title='Installs',
    yaxis=dict(type='log'),
)

scatter.show()

# --- EXTRACTING NESTED DATA FROM A COLUMN ---

# How many different types of genres are there? Can an app belong to more
# than one genre? Check what happens when you use value_counts() on a column
# with nested values. See if you can work around this problem by using the
# split() function and the DataFrame's stack() method.

# Number of genres.

print(len(df_apps_clean.Genres.unique()))

# Fix the issue of multiple categories being separated by the semicolon.

print(df_apps_clean.Genres.value_counts().sort_values(
    ascending=True,
)[:5])

# Split the strings on the semicolon & then stack them.

stack = df_apps_clean.Genres.str.split(
    ';',
    expand=True,
).stack()
print(f'We now have a single column with shape: {stack.shape}')
num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')

# --- COLOR SCALES IN PLOTLY CHARTS - COMPETITION IN GENRES ---

# Create this chart with the Series containing the genre data. Experiment wit
# the built-in color scales in Plotly. Find a way to set the color scale
# using the color_continuous_scale parameter. Find a way to make the color
# axis disappear by using coloraxis_showscale.

bar = px.bar(
    x=num_genres.index[:15],  # Index = Category Name
    y=num_genres.values[:15],  # Count
    title='Top Genres',
    hover_name=num_genres.index[:15],
    color=num_genres.values[:15],
    color_continuous_scale='Agsunset'
)

bar.update_layout(
    xaxis_title='Genre',
    yaxis_title='Number of Apps',
    coloraxis_showscale=False,
)

bar.show()

# --- GROUPED BAR CHARTS: FREE VS. PAID APPS PER CATEGORY ---

df_apps_clean.Type.value_counts()

df_free_vs_paid = df_apps_clean.groupby(
    ['Category', 'Type'],
    as_index=False,
).agg(
    {'App': pd.Series.count}
)

df_free_vs_paid.sort_values('App')

# Use Plotly Express to create a bar chart.

g_bar = px.bar(
    df_free_vs_paid,
    x='Category',
    y='App',
    title='Free vs. Paid Apps by Category',
    color='Type',
    barmode='group',
)

g_bar.update_layout(
    xaxis_title='Category',
    yaxis_title='Number of Apps',
    xaxis={'categoryorder': 'total descending'},
    yaxis=dict(type='log'),
)

g_bar.show()

# --- PLOTLY BOX PLOTS: LOST DOWNLOADS FOR PAID APPS ---

# Create a box plot that shows the number of Installs for free vs. paid apps.
# How does the median number of installations compare? Is the difference
# large or small?

box = px.box(
    df_apps_clean,
    y='Installs',
    x='Type',
    color='Type',
    notched=True,
    points='all',
    title='How Many Downloads are Paid Apps Giving Up?',
)

box.update_layout(
    yaxis=dict(type='log'),
)

box.show()

# --- PLOTLY BOX PLOTS: REVENUE BY APP CATEGORY ---

# Looking at the hover text, how much does the median app earn in the Tools
# category? If developing an Android app costs $30,000 or thereabouts,
# does the average photography app recoup its development costs?

df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']

box = px.box(
    df_paid_apps,
    x='Category',
    y='Revenue_Estimate',
    title='How Much Can Paid Apps Earn?',
)

box.update_layout(
    xaxis_title='Category',
    yaxis_title='Paid App (Ballpark) Revenue',
    xaxis={'categoryorder': 'min ascending'},
    yaxis=dict(type='log'),
)

box.show()

# --- HOW MUCH CAN YOU CHARGE? EXAMINE PAID APP PRICING STRATEGIES ---

# What is the median price for a paid app? Compare pricing by category by
# creating another box plot. This time, examine the prices of the paid apps.

df_paid_apps.Price.median()

box = px.box(
    df_paid_apps,
    x='Category',
    y='Price',
    title='Price per Category',
)

box.update_layout(
    xaxis_title='Category',
    yaxis_title='Paid App Price',
    xaxis={'categoryorder': 'max descending'},
    yaxis=dict(type='log')
)

box.show()
