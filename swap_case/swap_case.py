'''
Created on Mar 6, 2015

https://www.codeeval.com/open_challenges/96/

Write a program which swaps letters' case in a sentence. All non-letter 
characters should remain the same.
Input sample:

Your program should accept as its first argument a path to a filename. 
Input example is the following 

Hello world!
JavaScript language 1.8
A letter

Output sample:

Print results in the following way. 

hELLO WORLD!
jAVAsCRIPT LANGUAGE 1.8
a LETTER

@author: Grant Cahill
'''
import sys

def flip_case(line):
    line_list = list()
    for letter in line:
        if str(letter).islower():
            line_list.append(str(letter).upper())
        else:
            line_list.append(str(letter).lower())
            
    print ''.join(line_list)

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        line = line.strip()
        flip_case(line)
        
    file_obj.close()