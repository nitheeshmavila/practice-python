1#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""
def get_special_paths(dirname):
  special_files=[]
  paths = os.listdir(dirname)
  for filename in paths:
    match = re.search(r'__(\w+)__', filename)
    if match:
      special_files.append(os.path.abspath(os.path.join(dirname, filename)))
  return special_files

def copy_to(paths, to_dir):
  if not os.path.exists(to_dir):
    os.mkdir(to_dir)
  for p in paths:
    file_name = os.path.basename(p)
    shutil.copy(p, os.path.join(to_dir, file_name))
  
def zip_to(paths, zipfile):
  c = 'zip -j ' + zipfile + ' '.join(paths)
  print "Command I'm going to do:" + cmd
  (status, output) = commands.getstatusoutput(c)
  if status ==0:
    print "command executed succssesfully"
  else:
    sys.stderr.write(output)
    sys.exit(1)
   

   





def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[0]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[0]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  paths = []
  for dirname in args:
    paths.extend(get_special_paths(dirname))

  if todir:
    copy_to(paths, todir)
  elif tozip:
    zip_to(paths, tozip)

  
if __name__ == "__main__":
  main()
