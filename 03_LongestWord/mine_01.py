def LongestWord(sen): 
  L = sen.split()
  x = 0
  word = "sample"
  for i in range(len(L)):
    if len(L[i]) > x:
      x = len(L[i])
      word = L[i]
  return word
