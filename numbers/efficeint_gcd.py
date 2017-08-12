def gcd(m,n):
    # effieicent algorith to compute  gcd using euclid algorith with while
    if (m<n):
        (m,n)=(n,m)
    while (m%n) != 0:
        (m,n)=(n,m%n)
    return n
print(gcd(20,100))
