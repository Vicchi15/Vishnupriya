#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import re
import os
import shutil
import subprocess
import zipfile

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
  list=[]
  filenames=os.listdir(dir)
  for filename in filenames:
    special=re.search(r'__(\w+)__',filename)
    special=special.group()
    if(special):
      list.append(os.path.abspath(os.path.join(dir,filename))
  return list

def copy_to(paths,dir):
  target=dir
  if not os.paths.isdir(target):
    os.mkdir(target)
  for i in paths:
    shutil.copy(i,os.path.join(target,os.path.basename(i))
 
def zip_to(paths,zip_path):
  zip=zipfile.ZipFile(zip_path,"a")
  for i in paths:
    zip.write(i)
  zip.close()
    
  
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  for d in args:
    list=get_special_paths(d)
  if todir:
    copy_to(list,todir)
  if tozip:
    zip_to(list,tozip)
  
if __name__ == "__main__":
  main()
