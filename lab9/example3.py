def get_evens(nums):
  if len(nums) == 0:
    return 0
  else:
    if nums[0] % 2 == 0:
      retun get_evens(nums[1:]) + 1
    else:
      return get_evens(nums[1:])



print(get_evens())
