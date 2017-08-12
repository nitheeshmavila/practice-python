'''
Question 3 : Fibonacci 
 
author : Nitheesh M.N

'''
def fibonacci(n):
    ''' This function is a generator function for Fibonacci numbers'''
    a, b = 0, 1
    while n > 0:
        yield a
        a, b = b, a + b
        n -= 1

def main():
    n = int(input())
    if n >= 1 and n <= 10:
        for element  in fibonacci(n):
            print(element)

if __name__ == '__main__':
	main()

