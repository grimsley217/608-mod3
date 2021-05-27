#bonus.py
"""Uses the statistics module to calculate measures of dispersion."""

import statistics as stats
import random

#allows user to input the number of values and upper range of values
my_values=int(input('How many values do you want? '))
my_range=(1+ int(input('What is the max integer you want as an option? ')))
#you have to add +1 to the upper range value since the max value in range(0, x) is x-1

#creates empty list and assigns 100 random values to the list
rolls=[]
for i in range(my_values):
  z=random.randrange(0,my_range)
  rolls.append(z)

x=stats.pvariance(rolls)
y=stats.pstdev(rolls)

print(rolls)
print('The population variance is: ', x)
print('The standard deviation is: ', y)
