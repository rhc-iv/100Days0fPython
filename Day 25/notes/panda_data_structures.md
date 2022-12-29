# Panda Data Structures:

### DataFrames

A `DataFrame` in the `pandas` module is the entirety of the 
collection of data within the data file that is being accessed. In 
this course section, the [weather_data.csv](/Users/rhc.iv/Development/100 Days Of Python/Course Sections/Day 25/venv/weather_data.csv) 
file would be considered as a `DataFrame`. For more information, 
consult the official `pandas` [documentation](https://pandas.pydata.org/docs/reference/frame.html).

### Series

A `Series` in the `pandas` module is a single value set within our 
data file. Here is a link to the official `pandas` [documentation](https://pandas.pydata.org/docs/reference/series.html). 
So, 
using 
[weather_data.csv]
(venv/weather_data.csv),
if we wrote the following code:

```python

import pandas

data = pandas.read_csv("weather_data.csv")

print(data["temp"])
```
... then our resulting console output would be:

```
0    12
1    14
2    15
3    14
4    21
5    22
6    24
Name: temp, dtype: int64
```
