def front3(str):
  newStr = ' '
  
  if len(str) < 3:
    newStr = str[0:] * 3
    
  else:
    newStr = str[0:3] * 3
    
  return newStr
    
   

  
  

# strings are immutable! Set an empty string variable!  
# front is first 3 indices of string (capture front 3 indices and multiply by 3)

# if string < 3 chars
# front is whatever is available(capture entire string and *3)

# concatenate: string indices*3 + empty_str
# return empty_str to function

