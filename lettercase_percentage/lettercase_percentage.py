'''
Created on Feb 25, 2015

https://www.codeeval.com/open_challenges/147/

Your task is to write a program which determines (calculates) 
the percentage ratio of lowercase and uppercase letters.
Input sample:

Your program should accept a file as its first argument. Each 
line of input contains a string with uppercase and lowercase 
letters.

For example: 
thisTHIS
AAbbCCDDEE
N
UkJ

Output sample:

For each line of input, print the percentage ratio of uppercase 
and lowercase letters rounded to the second digit after the point.

For example: 
lowercase: 50.00 uppercase: 50.00
lowercase: 20.00 uppercase: 80.00
lowercase: 0.00 uppercase: 100.00
lowercase: 33.33 uppercase: 66.67

@author: Grant Cahill
'''
import sys

def case_percentage(word):
    upper = 0
    lower = 0
    total_length = len(word)
    
    for letter in word:
        if letter.isupper():
            upper += 1
        else:
            lower += 1
    low_percentage = float(lower) / float(total_length)
    up_percentage = float(upper) / float(total_length)
    low_percentage *= 100
    up_percentage *= 100
    print "lowercase: {:.2f} uppercase: {:.2f}".format(low_percentage, up_percentage)

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        line = line.strip()
        case_percentage(line)
    
    file_obj.close()