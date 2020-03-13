def near_hundred(n):
  """ 
  Given an int n, return True if it is within 10 of 100 or 200.
  Note: abs(num) computes the absolute value of a number.
  
  """
  # chk if n is within 10 units (up or down) of 100:
  if n > abs(89) and n < abs(111):
    return True

  # chk if n is within 10 units (up or down) of 200:
  elif n > abs(189) and n < abs(211):
    return True

  else:
    return False

# my alternatative answer:
# return( n > abs(89) and n < abs(111)) or (n > abs(189) and n < abs(211))
