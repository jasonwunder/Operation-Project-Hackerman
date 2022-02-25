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

# Function for creating a user generated list
def term_list():
    term_list = []
    #Check for first name 
    first_name = input("Enter targets first name: ")
    term_list.append(first_name)
    # Check for last name
    last_name = input("Enter targets last name: ")
    term_list.append(last_name)
    # Check for nickname
    nickname = input("Does the target have a known nickname? [y/n]")
    if nickname == "y":
        nn = input("Enter the targets nickname: ")
        term_list.append(nn)
    else:
        pass
    # Check for pets name   
    pet = input("Does the target have a pet? [y/n]")
    if pet == "y":
        pet_name = input("Enter pets name: ")
        term_list.append(pet_name)
    # Check for DOB
    dob = input("Do you know the targets DOB? [y/n] ")
    if dob == "y":
        dob_answ = input("Enter DOB in either of the following formats: [mmddyy] [mmddyyyy] [yy] [yyyy]: ")
        term_list.append(dob_answ)
    else:
        pass
    print("The terms you entered are: ", term_list)
    # Check for more terms
    more_terms = input("Are there any other terms you want to add? [y/n]")
    if more_terms == "y":
        n = int(input("Enter the number of terms: "))
        for i in range(0, n):
            print("Enter term number-{}: ".format(i + 1))
            # Add the element to the list
            term_list.append(input())
    print("The entered terms are: \n", term_list)

print(term_list())

# Have user validate if information is correct. If it is not have them enter the terms again.

# create a function that looks for date formats within the list

# Create a password generator that intergrates the list that was created by the user.

# function that make every other variable upper case or lower case

# loop that only upper cases first letter

# function that add all randomly generated birthdates to the end or begining of the element 

# the birthdates can come in 3 versions (1993) or (042893) or (93) len of DOB appendix should be 2 or 4 or 6

# function that add 1 random symbol to the begining or end of element

# common symbols "_" or "!" or "#" or "@" or "O" for "0"

