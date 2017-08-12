def print_list_inside_list(names):
 print (names) 
 for item in names:
  if isinstance(item,list):
    for item_inside_item in item:
      print (item_inside_item)
  else:
    print (item)

print_list_inside_list(['n','p','w',['f','g','fw','wf'],['fsf','ef']])
