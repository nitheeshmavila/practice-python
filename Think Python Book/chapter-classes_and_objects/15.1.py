#Exercise 15.1. Write a function called distance_between_points that takes two Points as ar-guments and returns the distance between them.
import math
class point:
   x=0
   y=0

def distance_between_points(p1,p2):
  dx=p2.x-p1.x
  dy=p2.y-p1.y
  distance=math.sqrt(dx**2-dy**2)
  return(distance)

def main():
  p1=point()
  p1.x=0
  p1.y=0
  p2=point()
  p2.x=10
  p2.x=10
  print(distance_between_points(p1,p2)) 

if __name__=='__main__':
  main()
