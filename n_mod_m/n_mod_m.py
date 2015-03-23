'''
Created on Mar 11, 2015

https://www.codeeval.com/open_challenges/62/

Given two integers N and M, calculate N Mod M (without using any inbuilt 
modulus operator).

Input sample:

Your program should accept as its first argument a path to a filename. 
Each line in this file contains two comma separated positive integers. 
E.g. 

20,6
2,3

You may assume M will never be zero.

Output sample:
2
2
2
0
7
1
3

Print out the value of N Mod M 

@author: Grant Cahill
'''
import sys, math

def find_mod(value, divider):
    div = math.trunc(value/divider)
    rem = value - (divider * div)
    return rem

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        line = line.strip()
        line_list = line.split(',')
        value = int(line_list[0])
        divider = int(line_list[1])
        print find_mod(value, divider)
    
    file_obj.close()