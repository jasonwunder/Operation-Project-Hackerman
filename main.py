import sys
import os
import itertools

# check the version of python that the user is using. if older than version 3, print an error message.
if (sys.version_info < (3, 0)):
    print('Error: Operation Project Hackerman only works with Python 3')
    sys.exit(1)

# Create a master list that every function will append to to make one big list
master_list = []
master_list2 = []

# Create a function for the user provied terms
def usr_input():
    term_list = []
    # Check for first name
    first_name = input("Enter targets first name: ")
    term_list.append(first_name)
    # Check for middle name
    middle_name = input("Do you know the targets middle name? [y/n] ")
    if middle_name == "y":
        mn_answ = input("Enter the targets middle name: ")
        term_list.append(mn_answ)
    else:
        pass
    # Check for last name
    last_name = input("Enter targets last name: ")
    term_list.append(last_name)
    # Check for nickname
    nickname = input("Does the target have a known nickname? [y/n]")
    if nickname == "y":
        nn_answ = input("Enter the targets nickname: ")
        term_list.append(nn_answ)
    else:
        pass
    # Check for pet
    pet = input("Does the target have a pet? [y/n]")
    if pet == "y":
        pet_name = input("Enter pets name: ")
        term_list.append(pet_name)
    # Check for DOB
    dob = input("Do you know the targets DOB? [y/n] ")
    if dob == "y":
        month = input("Enter the month of the DOB [mm]: ")
        term_list.append(month)
        day = input("Enter the day of the DOB [dd]: ")
        term_list.append(day)
        year = input("Enter the year of the DOB [yyyy]: ")
        term_list.append(year)
        year_short = input("Enter the year of the DOB again [yy]: ")
        term_list.append(year_short)
    else:
        pass
    # Check for phone number area code
    area_code = input("Do you know the targets phone number? [y/n]")
    if area_code == "y":
        ac_answ = input("Enter the area code of the phone number: [###] ")
        term_list.append(ac_answ)
    else:
        pass
    # Check for favorite sports team
    sports_team = input("Do you know the targets favorite sports team? [y/n]")
    if sports_team == "y":
        st_answ = input("Enter the team: ")
        term_list.append(st_answ)
    else:
        pass
    print("The terms you entered are: ", term_list)
    # Check for more terms
    more_terms = input("Are there any other terms you want to add? [y/n]")
    if more_terms == "y":
        n = int(input("Enter the number of terms: "))
        for i in range(0, n):
            print("Enter term number {}: ".format(i + 1))
            # Add the element to the list
            term_list.append(input())
    else:
        pass
    print("The entered terms are: \n", term_list)

    # call other functions for use of term_list
    term_combine(term_list)
    both_cap(term_list)
    sep_word(term_list, "!")
    sep_word(term_list, "_")
    sep_word(term_list, "%")
    sep_word(term_list, "$")
    sep_word(term_list, "@")
    sep_word(term_list, ".")
    sep_word(term_list, "-")
    sep_word(term_list, "*")
    sep_word(term_list, "&")
    change_char(term_list, "a", "@")
    change_char(term_list, "s", "$")
    change_char(term_list, "e", "3")
    change_char(term_list, "o", "0")
    change_char(term_list, "b", "9")
    change_char(term_list, "l", "1")
    change_char(term_list, "r", "4")
    change_char(term_list, "t", "7")
    change_char(term_list, "i", "1")

# Create function that takes in master list and combines elements together 
def term_combine(term_list):
    combine_list = []
    combine_list = list(''.join(entry)
        for entry in itertools.product(term_list, repeat=2))
    for elem in combine_list:
        master_list.append(elem)
    # print(combine_list)
    cap_char1(combine_list)

# Create a function that caps both words
def both_cap(term_list):
    cap_list = term_list.copy()
    cap_both_list = []
    for elem in cap_list:
        cap_both_list.append(elem.capitalize())
    cap_both_list = list(''.join(entry)
        for entry in itertools.product(cap_both_list, repeat=2))
    for elem in cap_both_list:
        master_list.append(elem)

# Create a list that takes in combine_list a caps the first letter of the element 
def cap_char1(combine_list):
    cap1_list = []
    for elem in combine_list:
        cap1_list.append(elem.capitalize())
    print(cap1_list)

# Function that adds a sym inbetween the two terms
def sep_word(term_list, value):
    sep_list = []
    sep_list = list(value.join(entry)
        for entry in itertools.product(term_list, repeat=2))
    for elem in sep_list:
        master_list.append(elem)

# Function that swaps out values
def change_char(term_list, old_value, new_value):
    new_list = master_list.copy()
    change_char_list = []
    for idx, value in enumerate(new_list):
        new_list[idx] = value.replace(old_value, new_value)
        master_list.append(new_list[idx])



# Have user validate if information is correct. If it is not have them enter the terms again.

# create a function that looks for date formats within the list

# Create a password generator that intergrates the list that was created by the user.

# function that make every other variable upper case or lower case

# loop that only upper cases first letter

# function that add all randomly generated birthdates to the end or begining of the element 

# the birthdates can come in 3 versions (1993) or (042893) or (93) len of DOB appendix should be 2 or 4 or 6

# function that add 1 random symbol to the begining or end of element

# common symbols "_" or "!" or "#" or "@" or "O" for "0"



#----------------------------------------------------------
#--------------TEST CODE HERE___________________________
#--------------------------------------------------------
usr_input()
for elem in master_list:
    print(elem)
for elem in master_list2:
    print(elem)
print(len(master_list))
print(len(master_list2))