#Project Euler Problem 1

import NumberTests #Ensure NumberTests.py is in the same directory

def main():
  n = 100001
  count = 0
  num = 1 
  while count < n:
    num += 1
    if isPrime(num):
      count += 1
  print(num)
   


if __name__ == '__main__':  # Fixed "__name__" check
  main()
