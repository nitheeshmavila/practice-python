'''
Exercise 8.6
---------------
'''



def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

def countOccuarance(word,letter):
    count = 0
    index = 0
    while index < len(word):
        if find(word, letter, index):
            count = count + 1
            index = find(word, letter, index) + 1
    return count
c = countOccuarance('nitheesh','e')
print(c)


