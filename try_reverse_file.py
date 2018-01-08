#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l',type=int, help='the number of lines to read')
parser.add_argument('--version','-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()
print(args.filename)


# print the file in reverse mode !
# first reverse lines in the file.
# then reverse each line.
try:
	f = open(args.filename)
except IOError as err:
	print("Error: file not found")
else:
    with f:
    	lines = f.readlines()
    	lines.reverse()	
    
    	if args.limit:
    		lines = lines[:args.limit]
    
    	for line in lines:
    		print(line.strip()[::-1])
finally:
	print("\n\nWe're finished ! \n\n")