# source: https://youtu.be/a9UrKTVEeZA 

import pandas as pd
from matplotlib import pyplot as plt

''' Plotting values (title, labels, legend)
'''
x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]

#plots on x and y axis respectively
'''
plt.plot(x, y)
plt.plot(x, z)
plt.title('test plot')
plt.xlabel('x')
plt.ylabel('y and z')
plt.legend(['this is y', 'this is z'])
plt.show()
'''

''' Loading data from .csv files
'''

'''
# 3 cols, 5 rows
sample_data = pd.read_csv('sample_data.csv')
print(sample_data)
print(type(sample_data))

# retrieving a specific column from the dataset
print(sample_data.column_c)

# it is a series
print(type(sample_data.column_c))

# returns the second value of the series
print(sample_data.column_c.iloc[1])

# column a on x axis and column b on the y axis

# using the 'o' argument, the plot changes to dots
plt.plot(sample_data.column_a, sample_data.column_b, 'o')
plt.plot(sample_data.column_a, sample_data.column_c)
plt.show()
'''

''' Analysis on a real dataset
    Columns: country, year, population
'''

# import the data
data = pd.read_csv('countries.csv')
print(data)

# compare the pop. growth in US and China
us = data[data.country == 'United States']

# explanation:
# data.country == 'United States' returns a series of True and False
# data[data.country == 'United States'] returns a portion of the data where the series is true

china = data[data.country == 'China']

plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population')
plt.show()

# percentage growth from first year (1952)
# set first year as 100%, show subsequent years relative to the first
# divide the populatuion series by the first year's population and multiply by 100 

plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(china.year, china.population / china.population.iloc[0] * 100)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population growth (first year = 100%)')
plt.show()
