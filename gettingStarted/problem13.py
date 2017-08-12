'''
Problem 13
----------
 Write a function istrcmp to compare two strings, ignoring the case.
'''
def istrcmp(s1, s2):
    return s1.lower()==s2.lower()

print(istrcmp('Nitheesh','NitheeSH'))
