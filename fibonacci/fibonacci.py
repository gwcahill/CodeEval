'''
Created on Mar 6, 2015

https://www.codeeval.com/open_challenges/22/

The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n-1) + F(n-2) when n>1.
Given an integer n>=0, print out the F(n).
Input sample:

The first argument will be a path to a filename containing integer numbers, one per line. E.g. 

5
12

Output sample:

Print to stdout, the fibonacci number, F(n). E.g. 

5
144

@author: Grant Cahill
'''
import sys

def find_fibonacci(target, fib_dict):
    if fib_dict.has_key(target):
        print fib_dict[target]
        return fib_dict[target]
    else:
        # find largest value in sequence thus far
        largest = 0
        for key, value in fib_dict.iteritems():
            if largest < key:
                largest = key
        # add new value to dict and repeat
        fib_dict[largest+1] = fib_dict[largest] + fib_dict[largest-1]
        find_fibonacci(target, fib_dict)
        

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    fib_dict = {0:0, 1:1, 2:1}
    
    for line in file_obj:
        target = int(line.strip())
        find_fibonacci(target, fib_dict)
        
    file_obj.close()