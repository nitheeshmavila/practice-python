 # renameDates.py - Renames filenames with American MM-DD-YYYY date format
   # to European DD-MM-YYYY.
import re ,os,shutil
def converting_date():
  for filename in os.listdir('.'):
    datepattern = re.compile(r"""^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""", re.VERBOSE)
    match=datepattern.search(filename)
    if match:
      month= match.group(2)
      day= match.group(4)
      year= match.group(6)
      newfilename=day+'-'+month+'-'+year
      path=os.path.abspath('.')
      print 'renaming %s to %s'%(filename,newfilename)
      shutil.move(filename,newfilename)
    else :
      continue
converting_date()
                  
