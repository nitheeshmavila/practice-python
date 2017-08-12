# f) Write a Python program to read an integer from the keyboard and  print the value of its LSB.

def print_lsb(n):
    lsb = n & 1
    print("LSB:",lsb)

def main():
    n = input('enter an integer\n')
    return print_lsb(int(n))
    
if __name__ == '__main__':
    main()
