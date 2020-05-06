def first_half(str):
  '''Given a string of even length, return the first half of the string
  such that the string "WooHoo" yields "Woo"'''
  newStr = ''
  newStr = newStr + str[0:len(str)//2]
  return newStr

res = first_half("testMed")
print(res)