#Exercise 17.3. Write a str method for the Point class. Create a Point object and print it.

class point(object):
  x=0.0
  y=0.0
  def __init__(self,x=0.0,y=0.0):
    self.x=x
    self.y=y
  def __str__(self):
    return('x=%d \n y=%d'%(self.x,self.y))

p=point(2,4)
print(p)
