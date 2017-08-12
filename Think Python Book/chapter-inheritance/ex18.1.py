#Exercise 18-1.
#Write a __cmp__ method for Time objects. Hint: you can use tuple comparison

class time(object):
  def __init__(self,hour=0,minute=0,second=0):
    self.hour=hour
    self.minute=minute
    self.second=second
  
  def __str__(self):
    return("%d:%d:%d"%(self.hour,self.minute,self.second))

  def __cmp__(self,other):
    t1=self.hour,self.minute,self.second
    t2=self.hour,self.minute,self.second
    return(cmp(t1,t2))
  
