'''
Created on Jan 30, 2015

Print out the sum of integers read from a file.

INPUT SAMPLE:

The first argument to the program will be a path to a filename 
containing a positive integer, one per line. E.g.

5
12

OUTPUT SAMPLE:

Print out the sum of all the integers read from the file. E.g.

17

@author: Grant Cahill
'''
import sys

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    sum_val = 0
    
    for line in file_obj:
        sum_val += int(str(line).strip())
    
    file_obj.close()
    
    print sum_val
    