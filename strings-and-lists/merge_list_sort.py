#it takes two list and merge them and sort it without using sort() function
def linear_merge(list1, list2):
  result = []
  while len(list1) and len(list2):
    if list1[0] < list2[0]:
      result.append(list1.pop(0))
    else:
      result.append(list2.pop(0))
  result.extend(list1)
  result.extend(list2)
  return result
