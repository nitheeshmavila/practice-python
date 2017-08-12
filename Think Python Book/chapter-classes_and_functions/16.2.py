#Exercise 16.2. Write a boolean function called is_after that takes two Time objects, t1 and t2 ,and returns True if t1 follows t2 chronologically and False otherwise. Challenge: don’t use an if statement.
import copy
class time:
  hour=0
  minut=0
  second=0

def is_after(t1,t2):
  if(t1.hour<t2.hour):
    return(True)
  elif t1.hour == t2.hour:
    if(t1.minut<t2.minut):
      return(True)
    elif(t1.minut==t2.minut):
      if(t1.second<t2.second):  
        return(True)
      else:
        return(False)
    else:
      return(False)

  else:
    return(False)

def main():
  t1=time()
  t2=copy.copy(t1)
  t1.hour=1
  t1.minut=23
  t1.second=59
  t2.hour=2
  t2.minut=23
  t2.second=45
  print(is_after(t1,t2))

if __name__=='__main__' :
  main()
