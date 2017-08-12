''' implementing unix command `head`
'''
import sys

fp = open(sys.argv[1])
i = 0
while(i < 10):
    for line in fp:
        print(line)
    i += 1

