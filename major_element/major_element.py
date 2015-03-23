'''
Created on Mar 5, 2015

https://www.codeeval.com/open_challenges/132/

The Major Element

Challenge Description:

The major element in a sequence with the length of L is the element which 
appears in a sequence more than L/2 times. The challenge is to find that 
element in a sequence.

Input sample:

Your program should accept as its first argument a path to a filename. 
Each line of the file contains a sequence of integers N separated by 
comma. E.g. 

92,19,19,76,19,21,19,85,19,19,19,94,19,19,22,67,83,19,19,54,59,1,19,19
92,11,30,92,1,11,92,38,92,92,43,92,92,51,92,36,97,92,92,92,43,22,84,92,92
4,79,89,98,48,42,39,79,55,70,21,39,98,16,96,2,10,24,14,47,0,50,95,20,95,48,50,12,42

Output sample:

For each sequence print out the major element or print "None" 
in case there is no such element. E.g. 

19
92
None

Constraints:
N is in range [0, 100]
L is in range [10000, 30000]
The number of test cases <= 40 

@author: Grant Cahill
'''
import sys

def group_elements(elem_list):
    group_dict = {}
    
    for item in elem_list:
        if group_dict.has_key(item):
            group_dict[item] += 1
        else:
            group_dict[item] = 1
    
    return group_dict

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        major = 0
        line = line.strip()
        line_list = line.split(',')
        for key, value in group_elements(line_list).iteritems():
            if value > len(line_list)/2:
                major = key
                break
            else:
                major = 'None'
                
        print major
        
    file_obj.close()