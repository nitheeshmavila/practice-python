'''
Exercise 7.3.
-------------
 To test the square root algorithm in this chapter, you could compare it with
math.sqrt . Write a function named test_square_root that prints a table like this:
<column 1>
1.0
2.0
3.0
4.0
5.0
6.0
7.0
8.0
9.0

<column 2>
1.0
1.41421356237
1.73205080757
2.0
2.2360679775
2.44948974278
2.64575131106
2.82842712475
3.0

<column 3>
1.0
1.41421356237
1.73205080757
2.0
2.2360679775
2.44948974278
2.64575131106
2.82842712475
3.0

<column 4> 
0.0
2.22044604925e-16
0.0
0.0
0.0
0.0
0.0
4.4408920985e-16
0.0

The first column is a number, a; the second column is the square root of a computed with the function
from Section 7.5; the third column is the square root computed by math.sqrt ; the fourth column is
the absolute value of the difference between the two estimates.
'''
import math

def squareRoot(a):
    x = 2
    while True:
#       print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y 
    return y

l = [1.0, 2.0, 3.0,
     4.0, 5.0, 6.0,
     7.0, 8.0, 9.0]
def testSquareRoot(l):
    for i in l:
        print('%f\t%f\t%f\t%f'%(i,
              squareRoot(i),
              math.sqrt(i), 
              squareRoot(i) - math.sqrt(i)))
    return 'Table shows square root '
print(testSquareRoot(l))
