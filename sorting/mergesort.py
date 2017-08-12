#merge sort
def merge_sort(a,l,r):#sorting the slice a[l:r]
  if r-l <= 1:
    return(a[l:r])
  if r-l > 1:
    mid=(l+r)//2
    L=merge_sort(a,l,mid)
    R=merge_sort(a,mid,r)
    return(merge(L,R))

def merge(l1,l2):#merging l1[0:m] and l2[0:n]
  (l,m,n,i,j)=([],len(l1),len(l2),0,0)#l is the merged list
  while i+j < m+n:
    if i==m:#case 1: l1 is empty
      l.append(l2[j])
      j=j+1
    elif j==n:#case2 :l2 is empty
      l.append(l1[i])
      i=i+1
    elif l1[i]<=l2[j] :#case 3 head of l2 is large
      l.append(l1[i])
      i=i+1
    elif l1[i]>l2[j]:#case 4: head of l1 is large
      l.append(l2[j])
      j=j+1
  return(l)


