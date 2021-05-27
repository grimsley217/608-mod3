#built-in-min-max.py
"""This calculates the min and max of given values."""

#function that calls the MAXIMUM value of 3 given values
def maximum(x, y, z):
  max_val=x #stores 1st value as the highest value, for now
  if y>x:
    max_val=y
  if z>y:
    max_val=z
  print('The maximum value is: ', max_val)


#function that calls the MAXIMUM value of any number of values
def minimum():
  list1=[] # creating an empty list
  x=int(input("MINIMUM: How many elements do you want in your list? "))
  for i in range(0, x):
    y = int(input("Enter next value: "))
    list1.append(y) #adds each inputted value to the list
  
  min_val=list1[0] # stores the 1st value (index 0) as the smallest value, for now
  for i in list1:
   if i<min_val:
     min_val=i
  print('The minimum value is: ', min_val)
