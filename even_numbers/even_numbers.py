'''
Created on Mar 6, 2015

https://www.codeeval.com/open_challenges/100/

Write a program which checks input numbers and determines whether a 
number is even or not.

Input sample:

Your program should accept as its first argument a path to a filename. 
Input example is the following 

701
4123
2936

Output sample:

Print 1 if the number is even or 0 if the number is odd. 

0
0
1

All numbers in input are integers > 0 and < 5000. 

@author: Grant Cahill
'''
import sys

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        val = int(line.strip())
        
        if val % 2 == 0:
            print 1
        else:
            print 0
            
    file_obj.close()