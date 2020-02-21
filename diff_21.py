def diff21(n):

  # Given an integer n, return the absolute value of the difference
  # between 21 and n.

  # Return double the absolute value of the difference if the given
  # integer n is greater than 21.

  # n is greater than 21
  if n > 21:
    return abs((21-n)*2)

  # n is less than or equal to 21
  else:
    return abs(n-21)
