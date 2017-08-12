""" l) Write a Python program to read two numbers A and N (0 <= N <= 31);
   print back A (in decimal) with its Nth bit cleared to 0 and all other bits
   unchanged."""


def clear_nth_bit(a,n):
    new = ~(1 << n) & a
    print("%d'th bit of %d is cleard and got  %d"%(n,a,new))

def main():
    A = input('enter a number\n')
    N = input('which bit(0 to 31) to clear?\n')  
    return clear_nth_bit(int(A),int(N))

if __name__=="__main__":
    main()
           
