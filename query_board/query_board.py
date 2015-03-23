'''
Created on Feb 26, 2015

https://www.codeeval.com/open_challenges/87/

There is a board (matrix). Every cell of the board contains 
one integer, which is 0 initially.

The next operations can be applied to the Query Board:
SetRow i x: it means that all values in the cells on row "i" have been changed to value "x" after this operation.
SetCol j x: it means that all values in the cells on column "j" have been changed to value "x" after this operation.
QueryRow i: it means that you should output the sum of values on row "i".
QueryCol j: it means that you should output the sum of values on column "j".

The board's dimensions are 256x256
"i" and "j" are integers from 0 to 255
"x" is an integer from 0 to 31
Input sample:

Your program should accept as its first argument a path to a filename. 
Each line in this file contains an operation of a query. E.g. 

SetCol 32 20
SetRow 15 7
SetRow 16 31
QueryCol 32
SetCol 2 14
QueryRow 10
SetCol 14 0
QueryRow 15
SetRow 10 1
QueryCol 2

Output sample:

For each query, output the answer of the query. E.g. 

5118
34
1792
3571

@author: Grant Cahill
'''
import sys

class Query:
    board = list()
    
    def __init__(self):
        self.board = list()
        
    def populate_row_col(self):
        init_value = 0
        max_value = 256
        
        zero_list = [init_value] * max_value
            
        for row in range(0, max_value):
            self.board.append(zero_list)
        
    def set_row(self, row, value):
        self.board[row] = [value] * 256
    
    def set_col(self, col, value):
        
        for x in range(0,len(self.board)):
            self.board[x][col] = value
    
    def query_row(self, row):
        total = 0
        
        for item in self.board[row]:
            total += item
            
        return total
    
    def query_col(self, col):
        total = 0
        
        for x in range(0,len(self.board)):
            total += self.board[x][col]
            
        return total
    

def main(input_file):
    query_board = Query()
    
    # initial population of zeroes
    query_board.populate_row_col()
    
    file_obj = open(input_file, 'r')
    
    for line in file_obj:
        line = line.strip()
        arg_list = line.split(' ')
        if len(arg_list) == 3:
            command = str(arg_list[0])
            row_col = int(arg_list[1])
            value   = int(arg_list[2])
            if command == 'SetRow':
                query_board.set_row(row_col, value)
            elif command == 'SetCol':
                query_board.set_col(row_col, value)
                
        elif len(arg_list) == 2:
            command = str(arg_list[0])
            row_col = int(arg_list[1])
            if command == 'QueryRow':
                print query_board.query_row(row_col)
            elif command == 'QueryCol':
                print query_board.query_col(row_col)
    file_obj.close()

if __name__ == '__main__':
    main(sys.argv[1])        
    