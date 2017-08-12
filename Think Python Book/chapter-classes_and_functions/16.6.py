# Write a function called mul_time that takes a Time object and a number and returns a new Time object that contains the product of the original Time and the number. Then use mul_time to write a function that takes a Time object that represents the finishing time in a race, and a number that represents the distance, and returns a Time object that represents the average pace (time per mile)

class Time:
  hour=0
  minute=0
  second=0

def time_to_int(time):
  minutes = time.hour * 60 + time.minute
  seconds = minutes * 60 + time.second
  return seconds

def int_to_time(seconds):
  time = Time()
  minutes, time.second = divmod(seconds, 60)
  time.hour, time.minute = divmod(minutes, 60)
  return time


def multime(time,n):
  newtime=Time()
  actual_seconds=time_to_int(time)
  result_second=actual_seconds*n
  newtime=int_to_time(result_second)
  return(newtime)

def race_time_per_mile(finishingtime,distance):
  finish_seconds=time_to_int(finishingtime)
  seconds_per_mile=finish_seconds/distance
  time_per_mile=Time()
  time_per_mile=int_to_time(seconds_per_mile)
  return(time_per_mile)
  
def main():
  time=Time()
  time.hour=1
  time.minute=34
  time.second=23
  newtime=Time()
  newtime=multime(time,10)
  print('old time -> %d:%d:%d \n new time -> %d:%d:%d'%(time.hour,time.minute,time.second,newtime.hour,newtime.minute,newtime.second))
  time_mile=Time()
  time_mile.hour=3
  time_mile.minute=23
  time_mile.second=35
  time_mile=race_time_per_mile(time_mile,5)
  print("time per mile -> %d:%d:%d"%(time_mile.hour,time_mile.minute,time_mile.second))
if __name__=='__main__':
  main()






