#NumberTests.py

def isThreeOrFive(n):
  """Returns boolean determination if number is multiple of 3 or 5"""

  if n % 3 == 0 or n % 5 == 0:
    return True
  else:
    return False
  
def getFactors(num):
  """Returns a list of all factors of given interger """
  factors = []
  for f in range(1,num):
    if num % f == 0:


def isPrime(p):
  """Returns boolean (True/False) if the value given is prime."""
  if p < 2:
    return False
  if p in (2, 3):
    return True
  if p % 2 == 0:
    return False
  
  for div in range(3, p// 2, 2):
    if p % div ==0:
      return False
    return True

def largest_prime_factor(n):
  """Returns the largest prime factor of a given number. """
  factor = 2
  while factor * factor <= n:
    if n % factor:
      factor += 1
    else:
      n //= factor
  return n # The last remaining factor is the largest prime factor
print(largest_prime_factor(600851475143))  #output should be 6857


def is_palindrome(n):
  return str(n) == str(n)[::-1]


def largest_palindrome():
  max_palinfrome = 0
  for a in range(100, 1000):
    for b in range(a, 1000):  #Avoid duplicate calculations
        product = a * b
        if is_palindrome(product) and product > max_palinfrome:
          return max_palinfrome
  
print(largest_palindrome()) # output should be 906609        



def isEven(n):
  """Returns boolean about given value being even."""

  if n % 2 == 0:
    return True
  else:
    return False

def addNum(numList, num):
  """Adds the given number to the given list. Does not add duplicate values."""

  numList.append(num)


def fibonacciSequence(value):
  """Returns a list of numbers in the fibonacci sequence up to the given value"""

  nums = [1, 2]
  size = 2
  n = nums[size - 1] + nums[size - 2]

  while n < value:
    addNum(nums, n)
    size = len(nums)
    n = nums[size - 1] + nums[size - 2]

  return nums

#Test your new functions in this main
def main():
  knownPrimes = [3, 7, 11, 13, 17]

  num = int(input("Enter a number: "))

  if isPrime(num):
    print("%d is a prime number" %(num))

  if isEven(num):
    print("%d is an even number" %(num))


if __name__ == '__main__':
    main()
