def pos_neg(a, b, negative):
    
    ''' 
    Given 2 int values, return True if one is negative and one is positive.
    If the parameter 'negative' is True, then return True only if both are negative.
    
    Restate problem:
    Given 2 numbers:
    return True if one of the numbers is negative and the other is positive.
    If parameter 'neagtive' is True, return True ONLY if both numbers are negative.
    
    '''
    
    # ensure all flowcharts are done for this problem.
    
    # negative == False
    if not negative:
      if (a < 0 and b >= 0) or (a >= 0 and b < 0):
        return True
      else:
        return False
      
    # if negative == True
    
    if negative:
      if (a < 0) and (b < 0):
        return True
      else:
        return False
        
  
    
      
      
    
  
      
