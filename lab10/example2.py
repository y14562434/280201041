def hailstone(x):
  if x == 1:
    return 1
  elif x % 2 == 0:
    print(x)
    return hailstone(x//2)
  else:
    print(x)
    return hailstone((x*3)+1)

print(hailstone(5))
  