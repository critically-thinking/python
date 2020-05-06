def non_start(a, b):
  """Given 2 strings, return the 2 strings concatenated together 
  with the first character of each string omitted. Strings should be 
  at least one (1) character in length"""

  newStr = a.split() + b.split()
  return newStr[0][1:] + newStr[1][1:]
