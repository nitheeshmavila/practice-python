'''
binary search
--------------
Assume the seq is sorted, seq is a list
function bsearch is a recursive version of binary search
'''

def bsearch(seq,v,l,r): 
   '''seq - sorted list
       v - value to be searched
       l - lower index
       r - higher index''' 

    print(seq,v,l,r)
    if r-l == 0 :
        return False
    mid=l+r//2
    if seq[mid]==v:
        return(v) 
    if seq[mid]>v:
        return(bsearch(seq,v,l,mid))
    else:
        return(bsearch(seq,v,mid,r))
