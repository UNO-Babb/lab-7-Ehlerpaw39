#Problem2.py
#Project Euler problem 2

from NumberTests import isEven
from NumberTests import fibonacciSequence # Corrected import statement

def main():
  nums = fibonacciSequence(4000001) # Fixed function call
  print (nums)
  total = 0
  for fib in nums:
    if isEven(fib): #Proper indentation
      total = total + fib
  
  print(total) # final answer

if __name__ == '__main__':  # Fixed "__name__" check
  main()
