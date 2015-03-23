'''
Created on Jan 30, 2015

Given path input, print file size in bytes.

@author: Grant Cahill
'''
import os, sys

if __name__ == '__main__':
    print os.path.getsize(sys.argv[1])