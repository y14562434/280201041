def square_sum(nums):
  sum = 0
  for i in nums:
    sum += i
  value = sum**2
  return value

a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
number = square_sum(a_list)
print(number)