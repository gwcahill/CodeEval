'''
Created on Mar 6, 2015

https://www.codeeval.com/open_challenges/18/

Given numbers x and n, where n is a power of 2, print out the smallest 
multiple of n which is greater than or equal to x. Do not use division 
or modulo operator.

Input sample:

The first argument will be a path to a filename containing a comma 
separated list of two integers, one list per line. E.g. 

13,8
17,16

Output sample:

Print to stdout, the smallest multiple of n which is greater than or 
equal to x, one per line. E.g. 

16
32

@author: Grant Cahill
'''
import sys

def find_multiple(test_val, mult_val):
    processing = True
    increment = mult_val
    
    while processing:
        if mult_val >= test_val:
            print mult_val
            processing = False
        else:
            mult_val += increment        

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        line_list = str(line.strip()).split(',')
        find_multiple(int(line_list[0]), int(line_list[1]))
    
    file_obj.close()