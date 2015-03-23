'''
Created on Feb 4, 2015

https://www.codeeval.com/open_challenges/13/

Write a program which removes specific characters from a 
string.

INPUT SAMPLE:

The first argument is a path to a file. The file contains 
the source strings and the characters that need to be scrubbed. 
Each source string and characters you need to scrub are delimited 
by comma.

For example:

how are you, abc
hello world, def

OUTPUT SAMPLE:

Print to stdout the scrubbed strings, one per line. 
Ensure that there are no trailing empty spaces on each 
line you print.

how re you
hllo worl

For example:

@author: Grant Cahill
'''
import sys, re
    
def remove_subsequence(parent, child):
    parent_list = list(parent)
    child_list = list(child)
    final_parent = list()
        
    for letter in child_list:
        for item in re.finditer(letter, parent):
            parent_list[item.start()] = '*'
            
    for c in parent_list:
        if c != '*':
            final_parent.append(c)
            
    return ''.join(final_parent)

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        item_list = str(line).strip().split(',')
        print remove_subsequence(item_list[0], item_list[1].strip())
    
    file_obj.close()