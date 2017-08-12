#Exercise 15.3. Write a version of move_rectangle that creates and returns a new Rectangle instead of modifying the old one.
import copy
class point:
  x=0.0
  y=0.0

class rectangle:
  width=0.0
  height=0.0
  corner=point()
  

def move_rectangle_modified(rect,dx,dy):
   new_rect=copy.copy(rect)
   new_rect.corner.x += dx
   new_rect.corner.y += dy
   return(new_rect)

def main():
  rect=rectangle()
  rect.width=10.0
  rect.height=20.0
  rect.corner.x=10.0
  rect.corner.y=10.0
  new_rect=move_rectangle_modified(rect,5.0,5.0)
  print(new_rect.corner.x,new_rect.corner.y)

if __name__=='__main__':
  main()


