'''
Created on Feb 25, 2015

Delta Time

Challenge Description:

You are given the pairs of time values. The values are in the HH:MM:SS 
format with leading zeros. Your task is to find out the time difference 
between the pairs.
Input sample:

The first argument is a file that contains lines with the time pairs.

For example: 
14:01:57 12:47:11
13:09:42 22:16:15
08:08:06 08:38:28
23:35:07 02:49:59
14:31:45 14:46:56

Output sample:

Print to stdout the time difference for each pair, one per line. You must 
format the time values in HH:MM:SS with leading zeros.

For example: 
01:14:46
09:06:33
00:30:22
20:45:08
00:15:11

@author: Grant Cahill
'''
import sys
from datetime import datetime

def time_diff(time_one, time_two):
    formatted_time = '%H:%M:%S'
    time_one = datetime.strptime(time_one, formatted_time)
    time_two = datetime.strptime(time_two, formatted_time)
    if time_one > time_two:
        delta = str(time_one - time_two)
        print str(datetime.strptime(delta, formatted_time)).split(' ')[1]
    else:
        delta = str(time_two - time_one)
        print str(datetime.strptime(delta, formatted_time)).split(' ')[1]

if __name__ == '__main__':
    file_obj = open(sys.argv[1], 'r')
    
    for line in file_obj:
        line = line.strip()
        time_one = line.split(' ')[0]
        time_two = line.split(' ')[1]
        time_diff(time_one, time_two)
        
    file_obj.close()