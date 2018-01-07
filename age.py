#!/usr/bin/python

# raw input is always string ...

name = raw_input("what is your name?")
birthdate = raw_input("what is your birthdate ")

# python will take care of input and set type accordingly......
age = input("How old are you?")

print("%s was born on %s" % (name, birthdate))
print("Half of your age is %s " % (age / 2))