"""m) Write a Python program to read two numbers A and N (0 <= N <= 31);
   print back the decimal value formed by the least significant
   N bits of A (for example, if A = 255 and  N=3,
   the answer should be 7 because the least significant N bits of 255 form
   the pattern 1 1 1 which is decimal  7).
"""
def extract_n_bits(a,n):
    new = ~(~0 << n) & a
    print("%d bits of %d are extracted and formed  %d"%(n,a,new))

def main():
    A = input('enter a number\n')
    N = input('how many least significant bits(0 to 31) to extract??\n')
    return extract_n_bits(int(A),int(N))

if __name__=="__main__":
    main()
          
