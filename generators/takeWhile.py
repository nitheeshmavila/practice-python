

def takeWhile(fn, a):
    for i in a:
        if fn(i):
            yield i
        else:
            break
   

a = [1,4,5,6,7,9,12,32,7,72,6]
for i in  takeWhile(lambda x : x < 10, a):
    print(i)
