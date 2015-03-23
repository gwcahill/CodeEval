'''
Created on Mar 2, 2015

https://www.codeeval.com/open_challenges/21/

Given a positive integer, find the sum of its constituent digits.
Input sample:

The first argument will be a path to a filename containing positive 
integers, one per line. E.g. 

23
496
12
1001

Output sample:

Print to stdout, the sum of the numbers that make up the integer, 
one per line. E.g. 

5
19
3
2

@author: Grant Cahill
'''
import sys

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        line = str(line).strip()
        count = 0
        for val in line:
            count += int(val)
            
        print count
    
    file_obj.close()