#Exercise B-3.
#Write a function called bisection that takes a sorted list and a target value and returns the index of the value in the list, if it’s there, or None if it’s not.


def bisection(seq,target,l,r): 
  if r-l == 0 :
    return(False)
  mid=l+r//2
  if seq[mid] == target:
    return(mid)
  if seq[mid] > target:
    return(bisection(seq,target,l,mid))
  else:
    return(bisection(seq,target,mid,r))

print(bisection([1,2,34,55,66],34,0,4))


 



































