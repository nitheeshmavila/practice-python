#Exercise 15.2. Write a function named move_rectangle that takes a Rectangle and two numbers named dx and dy . It should change the location of the rectangle by adding dx to the x coordinate of corner and adding dy to the y coordinate of corner .
class point:
  x=0.0
  y=0.0

class rectangle:
  width=0.0
  height=0.0
  corner=point()
  

def move_rectangle(rect,dx,dy):
   rect.corner.x += dx
   rect.corner.y += dy
   return(rect)

def main():
  rect=rectangle()
  rect.width=10.0
  rect.height=20.0
  rect.corner.x=10.0
  rect.corner.y=10.0
  new_rect=move_rectangle(rect,5.0,5.0)
  print(new_rect.corner.x,new_rect.corner.y)

if __name__=='__main__':
  main()










