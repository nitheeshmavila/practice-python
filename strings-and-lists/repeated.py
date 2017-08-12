'''Write a Python function repeated(l) that takes a list of immutable values as argument. The function should return the number of values that are repeated in the input list.

For instance, repeated([1,17,22,17,23,17]) should return 1 because only 1 value, 17 is repeated. Likewise repeated(["the","higher","you","climb","the","further","you","fall"]) is 2 becaues 2 values, "the" and "you", are repeated.'''

def repeated(l):
    repeatedElements = 0
    count = {}
    for i in l:
        count[i] = count.get(i, 0) + 1
    print(count)
    for key in count.keys():
        if count[key] > 1:
            repeatedElements += 1
    return repeatedElements

    



