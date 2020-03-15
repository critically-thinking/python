"""
Given a string, return a new string where
"not " has been added to the front. However,
if the string already begins with "not",
return the string unchanged.
"""

def not_string(str):
  
  addon = 'not '
  
  #if 'not' in str:
   # return str
  
  # prefix 'not' is at beginning of string - return string unchanged
  if str[0:3] == 'not':
    return str
  
  # prefix "not" is NOT the starting 3 characters of the string
  # concatenate the prefix "not" to the front of the string + return new value
  elif addon not in str:
    return addon + str
    






  
  
    
  
  
