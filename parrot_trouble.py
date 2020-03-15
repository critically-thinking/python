"""
# Trouble if parrot is talking AND hour is before 7 OR after 20 (return True for condition)
# No trouble if not talking and hour is before 7 OR before 20 (return False)
# if not talking and hour < =6 or hour < 20:
# parrot talking == True

"""
def parrot_trouble(talking, hour):
  if talking:
    if hour < 7 or hour > 20:
      return True
  return False
  
    
    
      

  
  
  
  


