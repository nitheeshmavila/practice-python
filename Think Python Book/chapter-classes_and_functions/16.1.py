#Exercise 16.1. Write a function called print_time that takes a Time object and prints it in the form hour:minute:second . Hint: the format sequence '%.2d' prints an integer using at least two digits, including a leading zero if necessary.
class time:
  hour=0
  minut=0
  second=0

def print_time(t):
  print('The time is %d:%d:%d' %(t.hour,t.minut,t.second))

def main():
  t=time()
  t.hour=1
  t.minut=20
  t.second=32
  print_time(t)

if __name__=='__main__':
  main()
