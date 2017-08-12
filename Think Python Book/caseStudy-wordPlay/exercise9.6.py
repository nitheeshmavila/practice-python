'''
Exercise 9-6.
--------------
Write a function called is_abecedarian that returns True if the letters in a word appear
in alphabetical order (double letters are ok). How many abecedarian words are there?'''

def isAlphabetical(word):
    # returns True if the letters in the word is alphabetical order
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True   


words = open('words.txt','r')
count = 0
for word in words:
    word = word.strip()
    if isAlphabetical(word):
        count += 1
        print(word)
print(count)
