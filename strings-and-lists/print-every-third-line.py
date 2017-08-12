'''
Write a Python program that reads input from the keyboard (standard input). The input will consist of some number of lines of text. The input will be terminated by a blank line. Your program should print every third line.

For instance, if the input is the following:

"Spot the mistake
in the following argument",
Jack challenged
1+(-1+1)+(-1+1)+... = (1+ -1)+(1+ -1)+...
so therefore,
1 = 0
??

then the output should be:

Jack challenged
1 = 0
'''
stop = ''
lineList = []
while(True):
    line = input()
    if line.strip() == stop:
        break
    lineList.append(line)

for i in range(2, len(lineList), 3):
    print(lineList[i])

    
    

