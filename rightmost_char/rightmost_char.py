'''
Created on Mar 6, 2015

https://www.codeeval.com/open_challenges/31/

Challenge Description:

You are given a string 'S' and a character 't'. Print out the position of 
the rightmost occurrence of 't' (case matters) in 'S' or -1 if there is none. 
The position to be printed out is zero based.
Input sample:

The first argument will ba a path to a filename, containing a string and a 
character, comma delimited, one per line. Ignore all empty lines in the input 
file. E.g. 

Hello World,r
Hello CodeEval,E

Output sample:

Print out the zero based position of the character 't' in string 'S', one per 
line. Do NOT print out empty lines between your output.
E.g. 

8
10

@author: Grant Cahill
'''
import sys

def find_rightmost(line, letter):
    location = -1
    for index, value in enumerate(line):
        if value == letter:
            location = index
            
    print location

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    line_list = list()
    
    for line in file_obj:
        line = line.strip()
        if (line != '\n') and (line != ''):
            line_list = line.split(',')
            find_rightmost(line_list[0], line_list[1])
            
    file_obj.close()