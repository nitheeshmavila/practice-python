'''
Problem 6: Complete the above implementation of json_encode by handling the case of dictionaries.

def json_encode(data):
    if isinstance(data, bool):
        if data:
            return "true"
        else:
            return "false"
    elif isinstance(data, (int, float)):
        return str(data)
    elif isinstance(data, str):
        return '"' + escape_string(data) + '"'
    elif isinstance(data, list):
        return "[" + ", ".join(json_encode(d) for d in data) + "]"
    else:
        raise TypeError("%s is not JSON serializable" % repr(data))

def escape_string(s):
    """Escapes double-quote, tab and new line characters in a string."""
    s = s.replace('"', '\\"')
    s = s.replace("\t", "\\t")
    s = s.replace("\n", "\\n")
    return s
This handles booleans, integers, strings, floats and lists, but doesn’t handle dictionaries yet. That is left an exercise to the readers.

If you notice the block of code that is handling lists, we are calling json_encode recursively for each element of the list, that is required because each element can be of any type, even a list or a dictionary.
'''

def json_encode(data):
    if isinstance(data, bool):
        if data:
            return "true"
        else:
            return "false"
    elif isinstance(data, (int, float)):
        return str(data)
    elif isinstance(data, str):
        return '"' + escape_string(data) + '"'
    elif isinstance(data, list):
        return "[" + ", ".join(json_encode(d) for d in data) + "]"
    elif isinstance(data,dict):
        e = '{'        
        for d in data:
          e += json_encode(d)
          e += ":"
          e += json_encode(data[d])+','
        e = e[:-1]
        e += '}'
        return e  
         
    else:
        raise TypeError("%s is not JSON serializable" % repr(data))

def escape_string(s):
    """Escapes double-quote, tab and new line characters in a string."""
    s = s.replace('"', '\\"')
    s = s.replace("\t", "\\t")
    s = s.replace("\n", "\\n")
    return s
a = json_encode([3,4,'f','g',{'h':3,'y':6}])
print(a)

