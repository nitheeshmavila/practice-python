def write_ticket():
 print "ticket is issued"
def police(speed,mood):
  if speed >= 80:
    print 'licence and registrationn please'
    if mood == 'terible' or speed >=100:
       print 'You have the right to remain silent.'
    elif mood == 'bad' or speed >= 90:
       print "I'm going to have to write you a ticket."
       write_ticket()
    else:
       print "Let's try to keep it under 80 ok?"
  else :
   print " have a nice journey, bye" 
