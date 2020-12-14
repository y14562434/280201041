def is_prime(n):
  if n < 2:
    return False
  elif n == 2:
    return True
  else:
    for i in range(2, n):
      if n % i == 0:
        return False
    return True

      
print(is_prime())  


def print_primes_betweeen(a,b):
  for n in range(a,b):
    if is_prime(n):
      print(n)