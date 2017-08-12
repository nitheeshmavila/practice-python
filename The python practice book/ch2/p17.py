'''
Problem 17: Write a program reverse.py to print lines of a file in reverse order.

$ cat she.txt
She sells seashells on the seashore;
The shells that she sells are seashells I'm sure.
So if she sells seashells on the seashore,
I'm sure that the shells are seashore shells.

$ python reverse.py she.txt
I'm sure that the shells are seashore shells.
So if she sells seashells on the seashore,
The shells that she sells are seashells I'm sure.
She sells seashells on the seashore;'''

fp = open('she.txt')
lines = []
for line in fp:
    lines.append(line)
for i in range(-1,-len(lines) -1, -1):
    print(lines[i])

    

