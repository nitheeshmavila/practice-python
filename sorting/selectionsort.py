def selectionsort(l):
  for start in range(len(l)):
    minimum_pos=start
    for i in range(start,len(l)):
      if l[i]<l[minimum_pos]:
        minimum_pos=i
    (l[minimum_pos],l[start])=(l[start],l[minimum_pos])
