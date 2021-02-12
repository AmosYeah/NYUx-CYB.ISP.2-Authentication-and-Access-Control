#!/usr/bin/python

import os, sys, stat

# Assuming A file named testfile.txt is provided in the same path as your python program named chgperms.py.  Write the chgperms.py so it will set the permissions on the file so the group has write and execute but not read.  No other permissions. 

# Set a file that allows “write” and “execute” by group.

os.chmod("testfile.txt", stat.S_IWGRP | stat.S_IXGRP)

print ("Changed mode successfully!!")