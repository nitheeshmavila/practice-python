import shelve,  sys
mcbShelf = shelve.open('mcb')
if sys.argv[1].lower() == 'delete'and len(sys.argv)==3:
  del mcbShelf[sys.argv[2]]

   
elif len(sys.argv) == 2:
  if sys.argv[1].lower()=='delete':
    for item  in mcbShelf.items():
      mcbShelf.clear()
    
