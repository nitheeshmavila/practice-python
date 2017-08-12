#Exercise 17.4. Write an add method for the Point class.


class point(object):
  x=0.0
  y=0.0
  def __init__(self,x=0.0,y=0.0):
    self.x=x
    self.y=y
  def __str__(self):
    return('x=%d \n y=%d'%(self.x,self.y))
  def __add__(self,other):
    result=point()
    result.x=self.x+other.x
    result.y=self.y+other.y
    return(result)

def main():
    p1=point(14,4)
    p2=point(5,4)
    print(p1+p2)

if __name__=='__main__':
  main()
