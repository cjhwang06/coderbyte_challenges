def FirstFactorial(num): 
  x = 1
  for i in range(num):
    x *= (i+1)
  return x
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print FirstFactorial(raw_input())           
