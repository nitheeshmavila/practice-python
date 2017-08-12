'''
Problem 3: Write a function unflatten_dict to do reverse of flatten_dict.

>>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
{'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}'''

def unflatten_dict(d,result=None):
    if result == None:
        result={}
    for key in d:
        if '.' in key:
            string='result'
            for i in key.split('.'):
                eval(string).setdefault(i,{})       # convert string to python object
                string += '[' + "'" + i + "'"  + ']'
            exec(string + ' = d[key]')          # run string as python expression
        else:
            result[key] = d[key]
    return result
