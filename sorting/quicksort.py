#quick sort

def quicksort(a,l,r):
  if r-l <= 1:
    return(a)
  yellow=l+1
  for green in range(l+1,r):
    if a[green]<=a[l]:
      (a[yellow],a[green])=(a[green],a[yellow])
      yellow=+1
  (a[l],a[yellow-1])=(a[yellow-1],a[l])
  quicksort(a,l,yellow-1)
  quicksort(a,yellow,r)
  return(a)


print(quicksort([3,34,54,355,56,456,4,535,5],0,5)) 
