'''
Problem 1: Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction'''

class ReverseIter:
    def __init__(self, l):
        self.l = l
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.l:
            return self.l.pop()
        else:
            raise StopIteration

for i in ReverseIter([123,323,23,24,2,3,4]):
   print(i)

