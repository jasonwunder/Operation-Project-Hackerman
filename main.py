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
dob = input("Do you know the targets DOB? [y/n] ")
if dob == "y":
    answer = input("Enter DOB in either of the following formats: [mmddyy] [mmddyyyy] [yy] [yyyy]: ")
    term_list.append(answer)
else:
    pass   
print("The terms you entered are: ", term_list)

# Have user validate if information is correct. If it is not have them enter the terms again.

# create a function that looks for date formats within the list

# Create a password generator that intergrates the list that was created by the user.

# function that make every other variable upper case or lower case

# loop that only upper cases first letter

# function that add all randomly generated birthdates to the end or begining of the element 

# the birthdates can come in 3 versions (1993) or (042893) or (93) len of DOB appendix should be 2 or 4 or 6

# function that add 1 random symbol to the begining or end of element

# common symbols "_" or "!" or "#" or "@" or "O" for "0"

