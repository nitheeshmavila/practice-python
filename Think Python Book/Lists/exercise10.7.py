'''
Exercise 10-7.
---------------
Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are
anagrams.'''


def anagrams(word, other):
    if len(word) != len(other):
        return False
    else:
        count = 0
        for ch in word:
            if ch in other:
                count += 1
        if count == len(other):
            return True
        else:
            return False


print(anagrams('sches','chess'))
