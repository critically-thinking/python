"""
Given a non-empty string and an int n, return
a new string where the char at index n has been
removed. The value of n will be a valid index of
a char in the original string (i.e. n will be in the 
range 0..len(str)-1 inclusive).

GOAL:
replace value of parameter variable(str) @ index[n]
w/ an empty str.
  
"""


def missing_char(str, n):
  newStr = ''
  
  #replace str value @ index n w/ value of newStr
  str = str.replace(str[n],newStr) 
  return str
 
  
  

