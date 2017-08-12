"""Exercise 17.5. Write an add method for Points that works with either a Point object or a tuple:

• If the second operand is a Point, the method should return a new Point whose x coordinate is
the sum of the x coordinates of the operands, and likewise for the y coordinates.

• If the second operand is a tuple, the method should add the first element of the tuple to the x coordinate and the second element to the y coordinate, and return a new Point with the result.

"""


class point(object):
  x=0.0
  y=0.0
  def __init__(self,x=0.0,y=0.0):
    self.x=x
    self.y=y

  def __str__(self):
    return('x=%d \n y=%d'%(self.x,self.y))
  
  def __add__(self,other):
    if isinstance(other,point):
      self.add_tuple(other)
    else:
      self.add_point(other)
  
  def add_tuple(self,other):
    result=point()
    result.x=self.x+other[0]
    result.y=self.y+other[1]
    return(result)

  def add_point(self,other):
    result=point()
    result.x=self.x+other.x
    result.y=self.y+other.y
    return(result)

def main():
    p1=point(14,4)
    p2=(3,4)
    print(p1+p2)

if __name__=='__main__':
  main()




