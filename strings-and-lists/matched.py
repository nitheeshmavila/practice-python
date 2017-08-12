def matched(s):
  p_list=[]
  for i in range(0,len(s)):
    if s[i] =='(':
      p_list.append('(')
    elif s[i] ==')' :
      if not p_list:
        return False
      else:
        del p_list[-1]
  if not p_list:
    return True
  else:
    return False
print (matched("()()(m"))
