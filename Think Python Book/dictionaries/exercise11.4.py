'''
Exercise 11-4.
---------------
Modify reverse_lookup so that it builds and returns a list of all keys that map to v , or
an empty list if there are none.'''

def reverseLookup(d, v):
    # d - dict, v - value
    keyList = []
    for k in d:
        if d[k] == v:
            keyList.append(k)
    return keyList


print(reverseLookup({'n':1, 'i':3, 'k':1}, 1))
