  """
  PROBLEM: Given 2 ints, a and b, return True if one of them
  is 10 or if their sun is 10.
  
  Restate problem:
  
  Given 2 numbers, return True if one of the numbers is equal to 10,
  or return True if the sum of the 2 given numbers is equal to 10.
  
  # Return value type: bool

  return True if at least one value is equivalent to 10 or
  return True if the sum of both values is equivalent to 10.
  otherwise return False for all other conditions!
  """

def makes10(a, b):
  if (a == 10 or b == 10) or a + b == 10: 
    return True
  else:
    return False
 
  
  
    
  
  
  
    
