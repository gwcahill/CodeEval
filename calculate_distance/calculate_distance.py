'''
Created on Mar 27, 2015

https://www.codeeval.com/open_challenges/99/

You have coordinates of 2 points and need to find the distance 
between them.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. 
Input example is the following

(25, 4) (1, -6)
(47, 43) (-25, -11)

All numbers in input are integers between -100 and 100.

OUTPUT SAMPLE:

Print results in the following way.

26
90

You don't need to round the results you receive. They must be integer numbers.

@author: Grant Cahill
'''
import sys
from math import sqrt

def two_point_distance(x_one, y_one, x_two, y_two):
    '''
    Distance between two points on a 2D plane is as follows:
    sqrt((delta_x)^2 + (delta_y)^2)
    '''
    delta_x = x_two - x_one
    delta_y = y_two - y_one
    x_sqr = delta_x * delta_x
    y_sqr = delta_y * delta_y
    distance = sqrt(x_sqr + y_sqr)
    
    return int(distance)

def create_num_list(line):
    '''
    Expect line in format of: (25, 4) (1, -6)
    '''
    num_list = list()
    
    first_left_paren = -1
    second_left_paren = -1
    first_right_paren = -1
    second_right_paren = len(line)-1
    
    first_left_not_found = True
    first_right_not_found = True
    
    for index, value in enumerate(line):
        if value == "(" and first_left_not_found:
            first_left_paren = index
            first_left_not_found = False
        if value == "(":
            second_left_paren = index
        if value == ")" and first_right_not_found:
            first_right_paren = index
            first_right_not_found = False
            
    first_pair = line[first_left_paren+1:first_right_paren]
    second_pair = line[second_left_paren+1:second_right_paren]
    
    first_pair_list = first_pair.split(",")
    second_pair_list = second_pair.split(",")
    
    num_list.append(int(first_pair_list[0].strip()))
    num_list.append(int(first_pair_list[1].strip()))
    num_list.append(int(second_pair_list[0].strip()))
    num_list.append(int(second_pair_list[1].strip()))
    
    return num_list

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        line = line.strip()
        num_list = create_num_list(line)
        print two_point_distance(num_list[0], num_list[1], num_list[2], num_list[3])
        
    file_obj.close()