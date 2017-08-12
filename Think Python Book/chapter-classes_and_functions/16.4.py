#Exercise 16.4.
class Time:
  hour=0
  minute=0
  seconds=0


def time_to_int(time):
  minutes = time.hour * 60 + time.minute
  seconds = minutes * 60 + time.second
  return seconds
def int_to_time(seconds):
  time = Time()
  minutes, time.second = divmod(seconds, 60)
  time.hour, time.minute = divmod(minutes, 60)
  return time


def incriment(time, seconds):
  newtime=Time()
  initial_second=time_to_int(time)
  total_seconds=initial_second+seconds
  new_time=int_to_time(total_seconds)
  return(new_time)

def main():
  time=Time()
  time.hour=0
  time.minut=0
  time.second=0
  seconds=60000
  newtime=Time()
  newtime=incriment(time,seconds)
  print('new te -> %d:%d:%d'%(newtime.hour,newtime.minute,newtime.second))

if __name__=='__main__':
  main()                                                                                                                                           
