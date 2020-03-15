"""
Given two int values, return their sum. Unless the two values are 
the same, then return double their sum

Given two integer values, return their sum.
If the two integer values are the same
return double their sum.
"""
def sum_double(a, b):
  if a == b:
    return (a+b)*2
  else:
    return a+b
