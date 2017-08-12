#l is the list , v is the element to be searched.if it is fouund retun the position of v, otherwise returns -1. if v has duplicates it only returns the last position of the duplicate.
def find_positions(v,l):
  pos=-1
  for i in range(len(l)):
    if l[i]==v:
      pos=i
  return(pos)


