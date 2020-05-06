def combo_string(a, b):

  # return string in form short + long + short, short strings should be
  #on the outside with the longer length strings on the inside.
  #The strings will not be the same length, but they may be empty(length 0).'''

    # both strings have length 0 or one string is empty:

    if len(a) == 0 and len(b) == 0:
        return a + b
    elif len(a) > 0 and len(b) == 0:
        return a
    elif len(b) > 0 and len(a) == 0:
        return b

    # both strings have values greater than 0:

    if len(a) < len(b):
        return a+b+a
    else:
        return b+a+b
