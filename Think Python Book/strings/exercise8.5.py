'''
Exercise 8.5.
------------- 
Encapsulate this code in a function named count , and generalize it so that it accepts the string and the letter as arguments.
program counts the number of times the a letter appears in a string.
'''
def count(string, letter):
     count =0
     for ch in string:
        if ch == letter:
            count += 1
     return count


