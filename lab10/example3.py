def sum_of_a_list(a_list):
  if len(a_list) == 0:
    return 0
  else:
    if isinstance(a_list, list):
      return sum_of_a_list(a_list[0]) sum_of_a_list(a_list[1:])
    else:
      return a_list[0] + sum_of_a_list(a_list[1:])

