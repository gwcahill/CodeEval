'''
Created on Feb 24, 2015

https://www.codeeval.com/open_challenges/93/

Write a program which capitalizes the first letter of each word in 
a sentence.

Input sample:

Your program should accept as its first argument a path to a filename. 
Input example is the following:

Hello world
javaScript language
a letter
1st thing

Output sample:

Print capitalized words in the following way. 

Hello World
JavaScript Language
A Letter
1st Thing

@author: Grant Cahill
'''
import sys

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        line_list = list()
        upper_list = list()
        # remove white space
        line = line.strip()
        # only proceed if line has content
        if len(line) > 0:
            line_list = line.split(' ')
            for word in line_list:
                if word[0].isdigit():
                    upper_list.append(word)
                else:
                    upper_list.append(word[0].upper() + word[1:])
                
            print ' '.join(upper_list)
    
    file_obj.close()