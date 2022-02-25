###################################################################################################
############# THIS IS NOT FOR MAIN PRODUCT#################
###################################################################################################
import sys
import os
import random

# check the version of python that the user is using. if older than version 3, print an error message.
if (sys.version_info < (3, 0)):
    print('Error: Operation Project Hackerman only works with Python 3')
    sys.exit(1)

#if sys.version_info < 3:
#    raise Exception("Sorry, Operation Project Hackerman only works with Python 3 ")

# Create a functionf for the user provied terms
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
def password_gen(list):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
    upper = True
    lower = True
    numbers = True
    sym = True
    all = ""
    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if numbers:
        all += digits
    if sym:
        all += symbols
    length = 15
    amount = 10
    for element in list:
        for i in range(amount):
            password = element.join(random.sample(all, length))
        print(password)
    return password

password = password_gen(term_list)
print(password)