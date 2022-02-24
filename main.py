from curses import termattrs
import sys
import os

# check the version of python that the user is using. if older than version 3, print an error message.
if (sys.version_info < (3, 0)):
    print('Error: Operation Project Hackerman only works with Python 3')
    sys.exit(1)

#if sys.version_info < 3:
#    raise Exception("Sorry, Operation Project Hackerman only works with Python 3 ")

# Create variables for what needs to be used in the password generator.
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!#$%&()*+,-./:;<=>?@[\\]^_`{|}~"

# Create a list of the user provied terms
term_list = []
# Input number of elements
n = int(input("Enter the number of terms you are using: "))

for i in range(0, n):
    print("Enter term number-{}: ".format(i + 1))
    # Add the element to the list
    term_list.append(input())
print("The entered terms are: \n", term_list)

# Have user validate if information is correct. If it is not have them enter the terms again.


# Create a password generator that intergrates the list that was created by the user.


