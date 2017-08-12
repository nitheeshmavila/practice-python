''m v16 '
problem 14: Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.

>>> unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
["python", "java"]'''

def unique(l,f):
    
