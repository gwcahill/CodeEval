'''
Created on Jan 30, 2015

In this challenge you need to find the longest word in a sentence. 
If the sentence has more than one word of the same length you 
should pick the first one. 

Input sample:

Your program should accept as its first argument a path to a 
filename. Input example is the following:

some line with text
another line

Each line has one or more words. Each word is separated by space char. 

Output sample:

Print the longest word in the following way. 

some
another

@author: Grant Cahill
'''
import sys

def long_word(line):
    longest = ""
    word_list = str(line).split(" ")
    for word in word_list:
        if len(word) > len(longest): 
            longest = word
    
    return longest

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        print long_word(str(line).strip())
    
    file_obj.close()