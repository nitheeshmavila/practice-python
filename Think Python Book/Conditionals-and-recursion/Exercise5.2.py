# Exercise 5.2. Write a function called do_n that takes a function object and a number, n , as arguments, and that calls the given function n times.

square = lambda x: x*x

def do_n(square, n):
    # return sum of squares of integers starting from 1 to n
    sumOfSquares = 0
    for i in range(1, n+1):
         sumOfSquares += square(i)
    return sumOfSquares
  
print(do_n(square, 1))
