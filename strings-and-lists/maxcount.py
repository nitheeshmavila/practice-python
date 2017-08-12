'''Write a Python function maxcount(l) that takes a list of immutable values as argument. The list could have repeated values. The function should return the number of times the most frequent value is repeated.

For instance, maxcount([1,17,31,17,22,17]) should return 3 because the most frequent value, 17, occurs 3 times. Likewise maxcount(["the","higher","you","climb","the","further","you","fall"]) is 2 becaues the most frequent values, "the" and "you" both occur 2 times.'''

import operator

def maxcount(l):
    count = {}
    for i in l:
        count[i] = count.get(i, 0) + 1
    count = sorted(count.items(), key = operator.itemgetter(1), reverse=True)
    return count[0][1]


print(maxcount([1,17,31,17,22,17]))
print(maxcount(["the","higher","you","climb","the","further","you","fall"]))       
