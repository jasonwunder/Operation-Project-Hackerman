###################################################################################################
############# THIS IS NOT FOR MAIN PRODUCT#################
###################################################################################################
import sys
import os
import random

# check the version of python that the user is using. if older than version 3, print an error message.
if (sys.version_info < (3, 5)):
    print('Error: Operation Project Hackerman only works with Python 3')
    sys.exit(1)

# if sys.version_info < 3:
#    raise Exception("Sorry, Operation Project Hackerman only works with Python 3 ")

# Create a function for the user provied terms
term_list = []
first_name = input("Enter targets first name: ")
term_list.append(first_name)

last_name = input("Enter targets last name: ")
term_list.append(last_name)

nickname = input("Does the target have a known nickname? [y/n]")
if nickname == "y":
    nn = input("Enter the targets nickname: ")
    term_list.append(nn)
else:
    pass

pet = input("Does the target have a pet? [y/n]")
if pet == "y":
    pet_name = input("Enter pets name: ")
    term_list.append(pet_name)

dob = input("Do you know the targets DOB? [y/n] ")
if dob == "y":
    dob_answ = input(
        "Enter DOB in either of the following formats: [mmddyy] [mmddyyyy] [yy] [yyyy]: ")
    term_list.append(dob_answ)
else:
    pass
print("The terms you entered are: ", term_list)
n = int(input("Enter the number of terms you are using: "))
for i in range(0, n):
    print("Enter term number-{}: ".format(i + 1))
    # Add the element to the list
    term_list.append(input())
print("The entered terms are: \n", term_list)
# Have user validate if information is correct. If it is not have them enter the terms again.

# create a function that looks for date formats within the list

# Create a password generator that intergrates the list that was created by the user.
