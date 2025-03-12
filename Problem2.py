#Problem2.py
#Project Euler problem 2

from NumberTests import isPrime

def main():
    limit = 200000
    total = 0
    for num in range(2, limit):
       num += 2
       if isPrime(num):
          toal += num
          print(total)
 
  

if __name__ == '__main__':  
  main()
