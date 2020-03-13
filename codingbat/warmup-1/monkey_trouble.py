def monkey_trouble(a_smile, b_smile):

  # 2 monkeys: monkey a, and mokey b
  # parameters a_smile and b_smile indicate if each monkey is smiling

  # We are in trouble if they are both smiling or
  # if neither of them are smiling.

  # Return True if we are in trouble.

  if a_smile and b_smile:  # both monkeys a / b smiling:
    return True
  elif not a_smile and not b_smile:  # neither monkey a/b is smiling
    return True
  return False  # all other conditions
