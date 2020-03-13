def not_string(str):
  
  addon = 'not '
  
  #if 'not' in str:
   # return str
  
  # prefix 'not' is at beginning of string - return string unchanged
  
  if str[0:3] == 'not':
    return str
  
  # prefix "not" is not the starting 3 characters of the string
  # concatenate the prefix "not" to the front of the string + return new value
  
  elif addon not in str:
    return addon + str
    
# Alternative solution (Probably expressed better):
'''
if str[0:3] == 'not':
  return str

# this condition explicitly adresses first 3 characters of string
as opposed to the original solution which only states
that the string "not" is not found anywhere within the string

elif str [0:3] != “not”:
  return addon + str
  
'''





  
  
    
  
  
