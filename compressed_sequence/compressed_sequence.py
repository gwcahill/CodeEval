'''
Created on Mar 5, 2015

https://www.codeeval.com/browse/128/

Compressed Sequence
Challenge Description:

Assume that someone dictates you a sequence of numbers, and 
you need to write it down. For brevity, he dictates it as follows: 
first he dictates the number of consecutive identical numbers, 
and then - the number itself.

For example:
The sequence below 

1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 2

is dictated as follows:

two times one, three times three, four times two, 
three times fourteen, three times eleven, one time two

and you have to write down the sequence

2 1 3 3 4 2 3 14 3 11 1 2

Your task is to write a program that compresses a given sequence using this approach.
Input sample:

Your program should accept a path to a file as its first argument that contains 
T number of lines. Each line is a test case represented by a sequence of integers 
with the length L, where each integer is N separated by a space. 

40 40 40 40 29 29 29 29 29 29 29 29 57 57 92 92 92 92 92 86 86 86 86 86 86 86 86 86 86
73 73 73 73 41 41 41 41 41 41 41 41 41 41
1 1 3 3 3 2 2 2 2 14 14 14 11 11 11 2
7

Output sample:

For each test case, print out a compressed sequence of numbers separated 
by a single space, one per line.

For example:

4 40 8 29 2 57 5 92 10 86
4 73 10 41
2 1 3 3 4 2 3 14 3 11 1 2
1 7

Constraints:
T is in a range from 20 to 50.
N is in a range from 0 to 99.
L is in a range from 1 to 400.

@author: Grant Cahill
'''
import sys

def build_compressed_structure(input_list):
    multiplier = 0
    value = 0
    old_item = -1
    results = list()
    new_list_found = True
    
    for item in input_list:
        if item == old_item:
            multiplier += 1
        else:
            if new_list_found:
                value = item
                multiplier = 1
            else:
                results.append(str(multiplier))
                results.append(str(value))
                value = item
                multiplier = 1
                
        old_item = item
        new_list_found = False
        
    # append last item in list results
    results.append(str(multiplier))
    results.append(str(value))    
    
    result_obj = ' '.join(results)
    
    return result_obj
        

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        line = line.strip()
        line_list = line.split(' ')
        print build_compressed_structure(line_list)
    
    file_obj.close()