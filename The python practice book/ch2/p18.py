'''
Problem 18: Write a program to print each line of a file in reverse order.

'''
lines = []
fp = open('she.txt')
for line in fp:
    print(line[::-1])
