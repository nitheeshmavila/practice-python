'implemetation of tail'
import sys

fp = open(sys.argv[1])
lines = []
for line in fp:
    line = line.strip()
    lines.append(line)
for line in lines[-1:-11:-1]:
    print(line)


