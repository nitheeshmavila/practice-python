'''Renaming a list of images according to the given rename style'''
import string
import time 
import os

photoFiles = ['img1.jpg',
              'img2.jpg',
              'img3.jpg',
              'img4.jpg',
              'img5.jpg']
class BatchRename(string.Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')
t = BatchRename(fmt)
#print('t:',t)
date = time.strftime('%d%b%y')
#print('date:',date)
for i, filename in enumerate(photoFiles):
    #print(i,filename)
    base, ext = os.path.splitext(filename)
    #print(base,ext)
    newname = t.substitute(d = date, n = i, f = ext)
    print('{0} --> {1}'.format(filename, newname))
