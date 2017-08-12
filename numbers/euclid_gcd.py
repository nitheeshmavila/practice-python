def gcd(m,n):#original euclid
 if(m<n):
  (m,n)=(n,m)
 if(m%n==0):
  return n
 else:
  return gcd(n,m%n)

