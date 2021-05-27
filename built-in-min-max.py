#built-in-min-max.py
"""This calculates the min and max of given values."""

#function that calls the MAXIMUM value of 3 given values
def maximum(x, y, z):
  max_val=x #assumes 1st value as the highest value, for now
  if y>x:
    max_val=y
  if z>y:
    max_val=z
  print('The maximum value is: ', max_val)

#function that calls the MAXIMUM value of any number of values
def minimum(x, y, *z):
  list1=[x, y, *z] #stores all inputted values into a list   
  min_val=list1[0] #assumes the 1st value (index 0) as the smallest value, for now
  for i in list1:
   if i<min_val:
     min_val=i
  print('The minimum value is: ', min_val)
