#l is the list , v is the element to be searched.if it is fouund return list of positon that v is in, otherwise returns -1.

def find_positions(v,l):
  positions=-1
  positions=[ i  for i in range(len(l)) if l[i]==v]
  return(positions)


