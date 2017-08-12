'''
Exercise 9.2
--------------
Write a function named avoids that takes a word and a string of forbidden letters, and
that returns True if the word doesn’t use any of the forbidden letters.
Modify your program to prompt the user to enter a string of forbidden letters and then
print the number of words that don’t contain any of them. Can you find a combination
of 5 forbidden letters that excludes the smallest number of words?'''

def avoids(forbidden, word):
    for ch in word:
        if ch in forbidden:
            return False
    return True

count = 0
words = open('words.txt','r')
forbidden = input('enter the forbidden string\n')
for word in words:
    if avoids(word, forbidden):
        count += 1
print("%d words that don’t contain any of letters in %s"%(count,forbidden))
