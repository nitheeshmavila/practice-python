def factors(n):
  fact_list=[]
  for i in range(1,n+1):
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
def sumprimes(l):
  count=0
  for i in l:
    if prime_check(i):
      count += i
  return count
d=[4,6,15,27]
print (sumprimes(d))   
