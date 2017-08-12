'''
Problem 2: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

>>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
{'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
'''

def flattenDict(d,result=None,prefix=''):
    if result == None:
        result = {}

    for key in d:
        if isinstance(d[key],dict):
            flattenDict(d[key],result,prefix + str(key) + '.')
        else:
            result[prefix+str(key)] = d[key]
    return result
print(flattenDict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))
    
        
