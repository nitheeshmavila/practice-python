<<<<<<< HEAD
#to get  the files in a file system
# with out using builtin walk()
=======

#to get  the files in a file system staring from 'dirname'
>>>>>>> c3fc5461da87f325579418a41607965b1e034836
import os
def walk(dirname):
  for name in os.listdir(dirname):
    p = os.path.join(dirname, name)
    if os.path.isfile(p):
      print(p)
    else:
      walk(p)
walk('/home/nitheesh')
