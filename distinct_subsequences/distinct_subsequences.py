'''
Created on Feb 3, 2015

DISTINCT SUBSEQUENCES
CHALLENGE DESCRIPTION:

A subsequence of a given sequence S consists of S with zero 
or more elements deleted. Formally, a sequence Z = z1z2..zk 
is a subsequence of X = x1x2...xm, if there exists a strictly 
increasing sequence of indicies of X such that for all j=1,2,...k 
we have Xij = Zj. E.g. Z=bcdb is a subsequence of X=abcbdab with 
corresponding index sequence <2,3,5,7>

INPUT SAMPLE:

Your program should accept as its first argument a path to a 
filename. Each line in this file contains two comma separated 
strings. The first is the sequence X and the second is the 
subsequence Z. E.g.

babgbag,bag
rabbbit,rabbit

OUTPUT SAMPLE:

Print out the number of distinct occurrences of Z in X as a 
subsequence E.g.

5
3

@author: Grant Cahill
'''
import sys, re

def is_subsequence(parent, child):
    if str(parent).find(child):
        return True
    else:
        return False
    
def find_distinct_subsequences(parent, child):
    '''
    Goal is to keep the distinct 'child' substring
    in sequence in the search through parent. This 
    can be done by:
        - Convert each string to a list
        - Search for all occurrences of each character of 
          child in parent.
    '''
    parent_list = list(parent)
    child_list = list(child)
    
    print "Searching %s for %s." % (parent, child)
        
    for letter in child_list:
        for item in re.finditer(letter, parent):
            print "%s found at %d." % (letter, item.start())
        

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        item_list = str(line).strip().split(',')
        if is_subsequence(item_list[0], item_list[1]):
            find_distinct_subsequences(item_list[0], item_list[1])
    
    file_obj.close()