def factors(n):
  fact_list=[]
  for i in xrange(1,n+1):
    if n%i==0:
      fact_list.append(i)
  return fact_list
print factors(100)
