#this script generate random numbers
#The function random returns a random float between 0.0 and 1.0 (including 0.0 but not 1.0).
import random
for i in range(10):
  x=random.random()
  print(x)
#-----------------------------
print(random.randint(10,20))#generate random numbers beetween two integers

#-----------------------------
#To choose an element from a sequence at random

t=[1,23,342,24,43,2,8,6,32]
print(random.choice(t))
