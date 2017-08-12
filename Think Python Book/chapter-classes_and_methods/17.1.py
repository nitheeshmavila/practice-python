"""Exercise 17.1. Rewrite time_to_int (from Section 16.4) as a method. It is probably not appro-
priate to rewrite time_to_int as a method; what object you would invoke it on?"""

class Time(object):
  hour=0
  minute=0
  second=0  
  def time_to_int(self):
    minutes = self.hour * 60 + self.minute
    seconds = minutes * 60 + self.second
    return seconds

def main():
  time=Time()
  time.hour=1
  time.minut=31
  time.second=13
  sec=Time.time_to_int(time)
  print(sec)

if __name__=='__main__':
  main()
