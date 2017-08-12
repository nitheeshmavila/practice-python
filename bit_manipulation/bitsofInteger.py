'''
This programe takes the bits of an integer'''

class Integer:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.t = self.n
        return self

    def __next__(self):
        if self.t == 0:
            raise StopIteration()
        else:
            i = self.t % 2
            self.t = self.t // 2
            return i

for i in Integer(512):
    print(i)
