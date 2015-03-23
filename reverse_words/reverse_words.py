'''
Created on Feb 9, 2015

Write a program which reverses the words in an input sentence.
Input sample:

The first argument is a file that contains multiple sentences, 
one per line. Empty lines are also possible.

For example: 
Hello World
Hello CodeEval

Output sample:

Print to stdout each sentence with the reversed words in it, 
one per line. Empty lines in the input should be ignored. 
Ensure that there are no trailing empty spaces in each line 
you print.

For example: 
World Hello
CodeEval Hello

@author: Grant Cahill
'''
import sys

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    word_list = list()
    
    for line in file_obj:
        if line != "\n":
            word_list.append(list(line.strip().split(" ")))
    
    for row in word_list:
        row.reverse()
        print ' '.join(row)
    
    file_obj.close()