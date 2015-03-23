'''
Created on Mar 2, 2015

https://www.codeeval.com/open_challenges/20/

Input sample:

The first argument will be a path to a filename containing sentences, one per line. 
You can assume all characters are from the english language. E.g. 

HELLO CODEEVAL
This is some text

Output sample:

Print to stdout, the lowercase version of the sentence, each on a new line. E.g. 

hello codeeval
this is some text

@author: Grant Cahill
'''
import sys

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        line = str(line).strip()
        print line.lower()
    
    file_obj.close()