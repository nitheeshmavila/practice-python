'''
Problem 9: Write a function permute to compute all possible permutations of elements of a given list.

>>> permute([1, 2, 3])
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]'''


permutation_list = []
def permute(list_, left = 0, right = None):
    if left == right:
        permutation_list.append(list_[:])
    else:
        for i in range(left, len(list_)):
            list_[left], list_[i] = list_[i], list_[left]
            permute(list_, left+1, len(list_))
            list_[left], list_[i] = list_[i], list_[left]
    return permutation_list


print(permute(list(range(1,11))))
