'''
Created on Mar 2, 2015

https://www.codeeval.com/open_challenges/104/

Having a string representation of a set of numbers you need to 
print this numbers.

All numbers are separated by semicolon. There are up to 20 numbers 
in one line. The numbers are "zero" to "nine"

Input sample:

Your program should accept as its first argument a path to a 
filename. Each line in this file is one test case. E.g. 

zero;two;five;seven;eight;four
three;seven;eight;nine;two

Output sample:

Print numbers in the following way: 

025784
37892

@author: Grant Cahill
'''
import sys

word_digit_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        line = str(line).strip()
        line_list = line.split(';')
        
        digit_conv = ''
        
        for elem in line_list:
            digit_conv += str(word_digit_dict[str(elem).lower()])
            
        print digit_conv
    
    file_obj.close()