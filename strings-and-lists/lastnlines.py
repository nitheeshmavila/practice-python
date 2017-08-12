'''Write a Python program that reads input from the keyboard (standard input). The input will consist of an even number of lines of text. The input will be terminated by a blank line. Suppose there are 2n lines of input. Your program should print out the last n lines of the input, i.e., the second half of the input, followed by the first n lines, i.e., the first half of the input.

E.g., if the input is the following:

our dear friend,
let's eat

then the output should be:

let's eat
our dear friend,'''

stopword = ''
lines = []
while(True):
    line = input()
    if line == stopword:
        break
    lines.append(line)
    
n = len(lines) // 2
for line in lines[n:]:
    print(line)

for line in lines[0:n]:
    print(line)




