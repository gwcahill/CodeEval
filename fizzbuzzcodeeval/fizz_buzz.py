'''
Created on Jan 30, 2015

Players generally sit in a circle. The first player says the number "1", 
and each player says next number in turn. However, any number divisible 
by X (for example, three) is replaced by the word fizz, and any divisible 
by Y (for example, five) by the word buzz. Numbers divisible by both become 
fizz buzz. A player who hesitates, or makes a mistake is eliminated 
from the game.

Write a program that prints out the final series of numbers where those 
divisible by X, Y and both are replaced by "F" for fizz, "B" for buzz 
and "FB" for fizz buzz.


Input sample:

Your program should accept a file as its first argument. The file contains 
multiple separated lines; each line contains 3 numbers that are space delimited. 
The first number is the first divider (X), the second number is the second 
divider (Y), and the third number is how far you should count (N). You may 
assume that the input file is formatted correctly and the numbers are valid 
positive integers. 

For example:
3 5 10
2 7 15

Output sample:

Print out the series 1 through N replacing numbers divisible by X with "F", 
numbers divisible by Y with "B" and numbers divisible by both with "FB". 
Since the input file contains multiple sets of values, your output should 
print out one line per set. Ensure that there are no trailing empty spaces 
in each line you print. 
1 2 F 4 B F 7 8 F B
1 F 3 F 5 F B F 9 F 11 F 13 FB 15

Constraints:

    The number of test cases <= 20
    "X" is in range [1, 20]
    "Y" is in range [1, 20]
    "N" is in range [21, 100]

@author: Grant Cahill
'''
import sys

def fizz_buzz(fizz_div, buzz_div, upper_val):
    fb_list = list()
    for num in range(1, upper_val):
        if (num % fizz_div == 0):
            if (num % buzz_div == 0):
                fb_list.append('FB')
            else:
                fb_list.append('F')
        elif (num % buzz_div == 0):
            if (num % fizz_div == 0):
                fb_list.append('FB')
            else:
                fb_list.append('B')
        else:
            fb_list.append(str(num))
    return fb_list

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        input_list = list(str(line).strip().split())
        buzzin_list = fizz_buzz(int(input_list[0]), int(input_list[1]), int(input_list[2])+1)
        
        print " ".join(buzzin_list)
    
    file_obj.close()