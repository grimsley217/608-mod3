#population-dispersion.py
"""Uses the statistics module to calculate measures of dispersion."""

import statistics as stats

#creates list of dice roll values to be easily used later
rolls=[1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

x=stats.pvariance(rolls)
y=stats.pstdev(rolls)

print(rolls)
print('The population variance is: ', x)
print('The standard deviation is: ', y)
