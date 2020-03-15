


  """
  Given an integer n, return the absolute value of the difference
  between 21 and n.
  Return double the absolute value of the difference if the given
  integer n is greater than 21.
  
  """


def diff21(n):
   # n is greater than 21
  if n > 21:
    return abs((21-n)*2)
    
  # n is less than or equal to 21
  else:
    return abs(n-21)
  
  
  



# return difference between n and 21
# if integer n is greater than 21 return double the difference between the 2 numbers
