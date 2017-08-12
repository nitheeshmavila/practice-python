'''
Question : 4

please run in Python3

'''

class Integer:
    ''' This class is for an iteratable object over an integer'''
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.t = self.n
        return self

    def __next__(self):
        if self.t == 0:
            raise StopIteration()
        else:
            i = self.t % 10
            self.t = self.t // 10
            return i

def main():
    count = 0
    oneHoles = {0,4,6,9}
    twoHoles = 8
    n = int(input())
    for i in Integer(n):
        print(i)
        if i in oneHoles:
            count += 1
        if i == twoHoles:
            count += 2
    print('no of holes in %d : %d'%(n, count))
	

if __name__ == "__main__":
	main()		
