def harmonic(n):
  if n == 1:
    return 1
  else:
    sum = (1 / n) + harmonic(n-1)
    return sum

print(harmonic(5))