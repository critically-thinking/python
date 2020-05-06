def without_end(str):
  """Given a string of at least length 2, return the string with the first
  and last characters stripped from it"""

  #.split() splits a string in to a list where each word is an item
  newStr = str.split()

  #index 0 gives access to list container
  #slice [1:len(str)-1] gives access to the string characters in container
  return newStr[0][1:len(str)-1]







