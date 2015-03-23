'''
Created on Feb 23, 2015

https://www.codeeval.com/open_challenges/167/

CHALLENGE DESCRIPTION:

You are given a text. Write a program which outputs its lines according to the following rules:

If line length is <= 55 characters, print it without any changes.
If the line length is > 55 characters, change it as follows:
- Trim the line to 40 characters.
- If there are spaces ' ' in the resulting string, trim it 
  once again to the last space (the space should be trimmed too).
- Add a string '... <Read More>' to the end of the resulting string and print it.

INPUT SAMPLE:

The first argument is a file. The file contains a text.

For example:
Tom exhibited.
Amy Lawrence was proud and glad, and she tried to make Tom see it in her face - but he wouldn't look.
Tom was tugging at a button-hole and looking sheepish.
Two thousand verses is a great many - very, very great many.
Tom's mouth watered for the apple, but he stuck to his work.

OUTPUT SAMPLE:

Print to stdout the text lines with their length limited according to the rules described above.

For example:
Tom exhibited.
Amy Lawrence was proud and glad, and... <Read More>
Tom was tugging at a button-hole and looking sheepish.
Two thousand verses is a great many -... <Read More>
Tom's mouth watered for the apple, but... <Read More>

@author: Grant Cahill
'''
import sys

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    line_list = list()
    
    space_list = list()
    
    for line in file_obj:
        space_list[:] = []
        space_found = False
        line = str(line).strip()
        if len(line) <= 55:
            line_list.append(line)
        elif len(line) > 300:
            continue
        else:
            temp = line[:40]
            # search string and trim to last space if space found
            for index, value in enumerate(temp):
                if value == ' ':
                    space_list.append(index)
                    space_found = True
            if space_found:
                temp = temp[:space_list[-1]]
            
            temp = temp.strip()
            temp += "... <Read More>"
            line_list.append(temp)
            
    for item in line_list:
        print item
    
    
    file_obj.close()