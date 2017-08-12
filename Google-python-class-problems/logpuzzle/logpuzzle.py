#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def url_key(u):
  match = re.search(r'-(\w+)-(\w+)\.\w+', u)
  if match:
    return match.group(2)
  else:
    return u



def read_urls(filename):
  underbar = filename.index('_')
  host = filename[underbar + 1:]
  url = {}
  f = open(filename)
  for l in f:
    match = re.search(r'"GET (\S+)', l)
    if match:
      path = match.group(1)
      if 'puzzle' in path:
        url['http://' + host + path] = 1
  return  sorted(url.keys(), key=url_key)
 


 
  

def download_images(img_urls, dest_dir):
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir) 
  index = file(os.path.join(dest_dir, 'index.html'), 'w')
  index.write('<html><body>\n')
  i = 0
  for img_url in img_urls:
    local_name = 'img%d' % i
    print 'Retrieving...', img_url
    urllib.urlretrieve(img_url, os.path.join(dest_dir, local_name))

    index.write('<img src="%s">' % (local_name,))
    i += 1

  index.write('\n</body></html>\n')
  index.close()


  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
