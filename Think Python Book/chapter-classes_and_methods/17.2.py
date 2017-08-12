#Exercise 17.2. Write an init method for the Point class that takes x and y as optional parameters and assigns them to the corresponding attributes.
class point(object):
  x=0.0
  y=0.0
  def __init__(self,x=0.0,y=0.0):
    self.x=x
    self.y=y
  def printp(self):
    print('x value -> %d \n y value -> %d'%(self.x,self.y))


a=point(2)
a.printp()
