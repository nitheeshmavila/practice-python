#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  

"""
  year=0
  f=open(filename,'rU')
  contents=f.read()
  match = re.search(r'(/w+/s/w+/s)(/d/d/d/d)',contents)
  if match:
    year=match.group()
  names=[]
  names.append(year)
    
  names_rank={}
  m = re.findall(r'<td>(/d+)</td><td>(/w+)</td><td>(/w+)</td>',contents)
  for item in m:
    (r,boyname,girlname)=item
    if boyname not in names_rank:
      names_rank[boyname]=r
    if girlname not in names_rank:
      names_rank[girlname]=r
  sorted_names=sorted(names_rank.keys())
  for name in sorted_names:
    names.append(name+' '+names_rank[name])
  return names
def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  for filename in args:
    names = extract_names(filename)
    t = '\n'.join(names)

    if summary:
      fileout = open(filename, 'w')
      fileout.write(t + '\n')
      fileout.close()
    else:
      print text

if __name__ == '__main__':
  main()

