'''
Created on Feb 24, 2015

https://www.codeeval.com/open_challenges/152/

Age distribution

Challenge Description:

You're responsible for providing a demographic report for your local 
school district based on age. To do this, you're going determine which 
'category' each person fits into based on their age.

The person's age will determine which category they should be in:

If they're from 0 to 2 the child should be with parents print : 'Still in Mama's arms'
If they're 3 or 4 and should be in preschool print : 'Preschool Maniac'
If they're from 5 to 11 and should be in elementary school print : 'Elementary school'
From 12 to 14: 'Middle school'
From 15 to 18: 'High school'
From 19 to 22: 'College'
From 23 to 65: 'Working for the man'
From 66 to 100: 'The Golden Years'
If the age of the person less than 0 or more than 100 - it might be an alien - print: "This program is for humans"

Input sample:

Your program should accept as its first argument a path to a filename. 
Each line of input contains one integer - age of the person: 
0
19

Output sample:

For each line of input print out where the person is: 
Still in Mama's arms
College

@author: Grant Cahill
'''
import sys

def demographic(age):
    if age < 0:
        print 'This program is for humans'
    elif (age >= 0) and (age <=2):
        print 'Still in Mama\'s arms'
    elif (age >= 3) and (age <=4):
        print 'Preschool Maniac'
    elif (age >= 5) and (age <=11):
        print 'Elementary school'
    elif (age >= 12) and (age <=14):
        print 'Middle school'
    elif (age >= 15) and (age <=18):
        print 'High school'
    elif (age >= 19) and (age <=22):
        print 'College'
    elif (age >= 23) and (age <=65):
        print 'Working for the man'
    elif (age >= 66) and (age <=100):
        print 'The Golden Years'
    else:
        print 'This program is for humans'
    

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        line = line.strip()
        demographic(int(line))
    
    file_obj.close()