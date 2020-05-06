def first_two(str):
  """Given a string return the string consisting of only its first two characters,
  the string "Hello" would yield "He". If the string is less than 2 characters,
  return the string unchanged, so the string "X" yields "X" and an empty string
  yields an empty string."""

  if len(str) < 2:
    return str
  else:
    return str[0:2]





