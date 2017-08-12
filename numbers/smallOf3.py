''' function takes 3 integers and return the smallest '''

def min3(x,y,z):
  if x <= y:
    if x <= z:
      minimum = x
    else:
      minimum = z
  elif y <= z:
    minimum = y
  else:
    minimum = z
  return(minimum)


print(min3(12,1,0))
print(min3(1,22,3))
print(min3(21,3,4))
