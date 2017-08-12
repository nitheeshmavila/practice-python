'''
Exercise 6.6
------------
Write a function called is_palindrome that takes a string argument and returns True if it
is a palindrome and False otherwise. Remember that you can use the built-in function len
to check the length of a string.'''

def isPalindrome(s):
    reverse = s[::-1]
    if s == reverse:
        return True
    else:
        return False


