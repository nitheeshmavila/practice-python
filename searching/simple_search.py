#l is the list , v is the element to be searched.if it is fouund return positon otherwise return -1 ,note that it only gives the last position if the number is has duplicate.

def simple_search(v,l):
  pos=-1
  for i in range(len(l)):
    if l[i]==v:
      pos=i
  return(pos)

