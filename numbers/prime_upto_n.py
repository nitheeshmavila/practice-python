def factors(n):
  fact_list=[]
  for i in xrange(1,n+1):
    if n%i==0:
      fact_list.append(i)
  return fact_list
def prime_check(p):
  fact_list=[]
  fact_list=factors(p)
  if fact_list==[1,p]:
    return True
  else:
    return False
def prime_upto(n):
  prime_list=[]
  for i in range(1,n+1):
    if prime_check(i):
      prime_list.append(i)
  return prime_list

