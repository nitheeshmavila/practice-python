'''
Problem 8: Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?

>>> cumulative_sum([1, 2, 3, 4])
[1, 3, 6, 10]
>>> cumulative_sum([4, 3, 2, 1])
[4, 7, 9, 10]'''

def cumulativeSum(l):
    sumList = []
    if type(l[0]) == str:
        s = ''
    else:
        s = 0
    for i in l:
        s += i
        sumList.append(s)
    return sumList
        

print(cumulativeSum([1,2,3,4]))
print(cumulativeSum(['mn','appu','nithi']))
