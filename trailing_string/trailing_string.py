'''
Created on Feb 2, 2015

There are two strings: A and B. Print 1 if string B occurs at 
the end of string A. Otherwise, print 0.

INPUT SAMPLE:

The first argument is a path to the input filename containing two 
comma-delimited strings, one per line. Ignore all empty lines in the 
input file.

For example:

Hello World,World
Hello CodeEval,CodeEval
San Francisco,San Jose

OUTPUT SAMPLE:

Print 1 if the second string occurs at the end of the first string. 
Otherwise, print 0.

For example:

1
1
0

@author: Grant Cahill
'''
import sys

def check_substring(first, second):
    if first[-len(second):] == second:
        return 1
    else:
        return 0
    

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        contents = line.strip()
        if contents != '':
            line_list = str(contents).split(',')
            print check_substring(line_list[0], line_list[1])
    
    file_obj.close()