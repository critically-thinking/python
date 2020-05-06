def make_abba(a, b):
  ''' function returns strings concatenated together in following order: abba,
  Ex. make_abba('hi','bye') --> hibyebyehi '''

  return (a+b) + (b+a)
