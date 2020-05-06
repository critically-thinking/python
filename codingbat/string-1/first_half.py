def non_start(a, b):

  newStr = a.split() + b.split()
  return newStr[0][1:] + newStr[1][1:]

res = non_start("test", "me")
print(res)
