'''
Created on Mar 12, 2015

https://www.codeeval.com/open_challenges/23/

Print out the grade school multiplication table up to 12*12.
Input sample:

There is no input for this program.
Output sample:

Print out the table in a matrix like fashion, each number formatted 
to a width of 4 (The numbers are right-aligned and strip out leading/trailing 
spaces on each line). The first 3 line will look like: 

1   2   3   4   5   6   7   8   9  10  11  12
2   4   6   8  10  12  14  16  18  20  22  24
3   6   9  12  15  18  21  24  27  30  33  36

@author: Grant Cahill
'''

def build_mult_table(max_value):
    mult_table = list()
    
    # create first line seeding the table
    first_line = list()
    for counter in range(1,max_value+1):
        first_line.append(counter)
        
    # create the table up to the max value
    for value in range(1,max_value+1):
        new_line = list()
        for multiplier in first_line:
            new_line.append(value*multiplier)
        mult_table.append(new_line)
    
    return mult_table

if __name__ == '__main__':
    max_value = 12
    mult_table = build_mult_table(max_value)
    
    for row in mult_table:
        line = ''
        for item in row:
            str_item = str(item)
            if len(str_item) == 1:
                line += '   ' + str(item)
            elif len(str_item) == 2:
                line += '  ' + str(item)
            elif len(str_item) == 3:
                line += ' ' + str(item)
            else:
                line += str(item)
            
        line = line.strip()
        print line