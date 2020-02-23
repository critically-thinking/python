def front_back(str):
  
  ''' 
    # grab last element of string 
    # concatenate to string slice starting @ 2nd element of string running 
    # the length of the string EXCLUDING the final element
    # concatenate length of the string EXCLUDING the final element to the 
    # very first element of the string (str[0])
  '''
  
  if len(str)==1 or len(str)==0: # if len str is equal to 1 or 0...
    return str
  elif len(str) > 1:# if len str is greater than 1...
  
    return str[-1] + str[1:len(str)-1] + str[0]
    
    
  
  
