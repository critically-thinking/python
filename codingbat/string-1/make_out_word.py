def make_out_word(out, word):
  ''' returns new string where the word is in the middle of the out string
  ex. make_out_word(out,word) --> '<<word>>' '''

  return out[:2] + word + out[2:]
