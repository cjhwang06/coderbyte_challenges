def FirstReverse(a): 
 original_str = a
 return a[::-1]
 #This is extended slice syntax. It works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string. More here: https://docs.python.org/2/whatsnew/2.3.html#extended-slices

print FirstReverse(raw_input())   
