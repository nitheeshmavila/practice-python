"""g) Write a Python program to read two integers: A and N from the keyboard.
   The program should print value of N'th bit of A (LSB is bit0, the bit to the
   immediate left of the LSB is bit1 and so on ...). The program should use
   bit operations (and NOT arithmetic operations) to do this. All the remaining
   programs in this section MUST also use bit operations."""


def print_nth_bit(a,n):
    "this function takes two integers a and n and prints the nth bit of a"
    n_bit = (a >> n) & 1
    print("%d'th bit of %d : %d"%(n,a,n_bit))

def main():
    "this function takes two input from user and calls the print_nth_bit()"
    A = input('enter a number\n')
    N = input('which bit to print?\n')
    return print_nth_bit(int(A),int(N))

if __name__ == "__main__":
    main()
