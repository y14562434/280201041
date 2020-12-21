def get_reversed(a_list):
  if len(a_list) == 0:
    return []
  else:
    return [a_list[-1]] + get_reversed(a_list[:-1])

test_l = [1,2,3]
reversed_test = get_reversed(test_l)

print(reversed_test)
