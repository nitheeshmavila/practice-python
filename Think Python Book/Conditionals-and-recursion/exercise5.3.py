'''
Exercise 5.3.
------------
 Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
a^n + b^n = c^n
for any values of n greater than 2.
1. Write a function named check_fermat that takes four parameters— a , b , c and n —and that
checks to see if Fermat’s theorem holds. If n is greater than 2 and it turns out to be true that
a^n + b^n = c^n
the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
print, “No, that doesn’t work.”
2. Write a function that prompts the user to input values for a , b , c and n , convert them to
integers, and uses check_fermat to check whether they violate Fermat’s theorem.'''

def checkFermats(a, b, c, n):
     # checks fermats theorem 
     if n > 2:
        if a**n + b**n == c**n:
            return 'Holy smokes, Fermat was wrong!'
        else:
            return "yes! Fermat was right"
        
def inputValues():
    a = input('enter a\n')
    b = input('enter b\n')
    c = input('enter c\n')
    n = input('enter n\n')
    return checkFermats(int(a), int(b), int(c), int(n))

print(inputValues())

