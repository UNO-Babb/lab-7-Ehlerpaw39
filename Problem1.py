#Project Euler Problem 1

import NumberTests #Ensure NumberTests.py is in the same directory

def main():
  total = 0
  for i in range(1001): # Loops from 0 to 1000
    if NumberTests.isThreeOrFive(i): # Fixed function name
      total += i

  print(total)  # Prints the sum of all multiples of 3 or 5 below 1000


if __name__ == '__main__':  # Fixed "__name__" check
  main()
