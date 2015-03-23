'''
Created on Jan 30, 2015

https://www.codeeval.com/open_challenges/2/

Write a program which reads a file and prints to stdout the 
specified number of the longest lines that are sorted based 
on their length in descending order.

INPUT SAMPLE:

Your program should accept a path to a file as its first argument. 
The file contains multiple lines. The first line indicates the number 
of lines you should output, the other lines are of different length and 
are presented randomly. You may assume that the input file is formatted 
correctly and the number in the first line is a valid positive integer.

For example:
2
Hello World
CodeEval
Quick Fox
A
San Francisco

OUTPUT SAMPLE:

Print out the longest lines limited by specified number and sorted 
by their length in descending order.

For example:
San Francisco
Hello World

@author: Grant Cahill
'''
import sys

def sort_lines(lines_list):
    sorted_elements = list()
    
    for line in sorted(lines_list, key=lambda line: len(line), reverse=True):
        sorted_elements.append(line)
    
    return sorted_elements

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    lines_list = list()
    
    # read in lines from file object
    for line in file_obj:
        lines_list.append(str(line).strip())

    # remove first element
    line_limit = int(lines_list.pop(0))
    
    # sort the lines
    sorted_lines = sort_lines(lines_list)
    
    # print out the number of lines based on sorted limit
    counter = 0
    while counter < line_limit:
        print sorted_lines[counter]
        counter += 1
    
    
    file_obj.close()