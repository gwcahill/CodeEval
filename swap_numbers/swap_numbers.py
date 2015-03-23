'''
Created on Mar 6, 2015

https://www.codeeval.com/open_challenges/112/

You are given a list of numbers which is supplemented with positions 
that have to be swapped.

Input sample:

Your program should accept as its first argument a path to a filename. 
Input example is the following 

1 2 3 4 5 6 7 8 9 : 0-8
1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3

As you can see a colon separates numbers with positions.
Positions start with 0.
You have to process positions left to right. In the example above 
(2nd line) first you process 0-1, then 1-3.

Output sample:

Print the lists in the following way. 

9 2 3 4 5 6 7 8 1
2 4 3 1 5 6 7 8 9 10

@author: Grant Cahill
'''
import sys

def swap_list_items(num_list, swap_list):
    for swap in swap_list:
        first_pos = int(swap.split('-')[0])
        second_pos = int(swap.split('-')[1])
        
        first_val = num_list[first_pos]
        second_val = num_list[second_pos]
        
        num_list[first_pos] = second_val
        num_list[second_pos] = first_val
        
    print ' '.join(num_list)

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        line = line.strip()
        line_list = line.strip().split(':')
        num_list = line_list[0].strip().split(' ')
        swap_list = line_list[1].strip().split(',')
        swap_list_items(num_list, swap_list)
        
    file_obj.close()