'''
This programe takes an integer n  from keyboard and prints first n terms of the fibonacci series'''

class Fibonacci:
    def __init__(self, n):
        self.n = n # where n is the no of terms
    
    def __iter__(self):
        self.a = 0
        self.b = 1
        self.counter = 0
        return self
    
    def __next__(self):
        f = self.a
        if self.counter >= self.n:
            raise StopIteration()
        else:
            self.a, self.b = self.b, self.a + self.b
            self.counter += 1
        return f

def main():
    n = int(input())
    for i in Fibonacci(n):
        print(i)
                
if __name__ == '__main__':
    main()   


