#!/usr/bin/python

import os

xmen_file = open('xmen.txt')

# print(xmen_file.read())

for line in xmen_file:
	print(line)

xmen_file.close()

# open with "w" will open file to write 
# "r+" will open file for read and write
# so use seek to the end of the file and set cursor there and begin to write!

# xmen_file = open('xmen.txt', "w")
xmen_file = open('xmen.txt', "r+")

xmen_file.seek(-1, os.SEEK_END)
xmen_file.write("\nBeast\n")
xmen_file.write("Phoenix\n")

xmen_file.close()

# you don't have to use "r+"
# you can just use 'a' for append the file

xmen_file = open('xmen.txt', 'a')

xmen_file.writelines(['Morph\n', 'Rouge\n'])

xmen_file.close()

# you can use with to create a block , and it will take care of all the close file steps

with open('xmen.txt', 'a') as xmen_file:
	xmen_file.write('Professor Xavier\n')