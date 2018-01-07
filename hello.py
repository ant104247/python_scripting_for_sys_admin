#!/usr/bin/python
# this is a comment !
print("Hello, World !")

count = 0
while count < 10:
	if count % 2 == 0:
		count += 1
		continue
	print("We're counting odd numbers %s" % count)
	count += 1
