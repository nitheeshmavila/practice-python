#Walk a directory tree and archive just files with certain extensions, such as .txt or .py, and nothing else  to compressed ZIP archives

import os,zipfile
def backup(folder):
  folder = os.path.abspath(folder) # make sure folder is absolute
#  print folder
  number = 1
  while True:
    zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
    #print zipFilename
    if not os.path.exists(zipFilename):
      break
    number = number + 1
  print "creating a new zip file %s"%(zipFilename) 
  newzipfile=zipfile.ZipFile(zipFilename,'w')
  print newzipfile
  for foldername, subfolders, filenames in os.walk(folder):
      print('Adding files in %s...' % (foldername))
      newzipfile.write(foldername)
      for filename in filenames:
        if filename.endswith('.txt') or filename.endswith('.py'):
          newBase = os.path.basename(folder) + '_'
          if filename.startswith(newBase) and filename.endswith('.zip'):
            continue   
          newzipfile.write(os.path.join(foldername, filename))
  newzipfile.close()
      
backup('.')



