def insort(seq):
  for sliceend in range(len(seq)):
    pos=sliceend
    while pos > 0 and seq[pos]<seq[pos-1]:
      (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
      pos=pos-1
