#! /usr/bin/python
from doctest import master
import re
import sys
import os
import random
import itertools
from turtle import position
from typing import final
from tqdm import tqdm


reset = '\033[0m'
bold = '\033[01m'
disable = '\033[02m'
underline = '\033[04m'
red = '\033[31m'
lightgreen = '\033[92m'
yellow = '\033[93m'
red_bold = '\033[31m' + '\033[01m'


print(red + """\
 ██████╗ ██████╗ ███████╗██████╗  █████╗ ████████╗██╗ ██████╗ ███╗   ██╗     
██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║     
██║   ██║██████╔╝█████╗  ██████╔╝███████║   ██║   ██║██║   ██║██╔██╗ ██║     
██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║   ██║   ██║██║   ██║██║╚██╗██║     
╚██████╔╝██║     ███████╗██║  ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║     
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝     
██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗                   
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝                   
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║                      
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║                      
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║                      
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝                      
██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗████╗ ████║██╔══██╗████╗  ██║
███████║███████║██║     █████╔╝ █████╗  ██████╔╝██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝                                                                             
                    """ + reset)
# check the version of python that the user is using. if older than version 3, print an error message.
if (sys.version_info < (3, 5)):
    print(red + 'Error: Operation Project Hackerman only works with Python 3' + reset)
    sys.exit(1)

# class colors:


# bold_red = "\033[1;31;40m"
print(bold + "Operation Project Hackerman - Version 1.0 \nWelcome \nThis tool requires that you know some information about the target." + reset)
contin = input(red + bold + "Select yes to continue: " + reset + "[y/n] ")
if contin == "y":
    loop = tqdm(total=5000, position=0, leave=False)
    for k in range(5000):
        loop.set_description("Loading...".format(k))
        loop.update(1)
    loop.close()
# Create a function for the user provied terms
def usr_input():
    master_list = []
    file_name = input(red_bold + "Enter name for output file: " + reset)
    term_list = []
    # Check for first name
    first_name = input(red_bold + "Enter targets first name: " + reset)
    term_list.append(first_name)
    # Check for middle name
    middle_name = input(red_bold + "Do you know the targets middle name? " + reset + "[y/n] ")
    if middle_name == "y":
        mn_answ = input(red_bold + "Enter the targets middle name: " + reset)
        term_list.append(mn_answ)
    else:
        pass
    # Check for last name
    last_name = input(red_bold + "Enter targets last name: " + reset)
    term_list.append(last_name)
    # Check for nickname
    nickname = input(red_bold + "Does the target have a known nickname? " + reset + "[y/n] ")
    if nickname == "y":
        nn_answ = input(red_bold + "Enter the targets nickname: " + reset)
        term_list.append(nn_answ)
    else:
        pass
    # Check for pet
    pet = input(red_bold + "Does the target have a pet? " + reset + "[y/n] ")
    if pet == "y":
        pet_name = input(red_bold + "Enter pets name: " + reset)
        term_list.append(pet_name)
    # Check for DOB
    dob = input(red_bold + "Do you know the targets DOB? " + reset + "[y/n] ")
    if dob == "y":
        month = input(red_bold + "Enter the month of the DOB " + reset + "[mm]: ")
        term_list.append(month)
        day = input(red_bold + "Enter the day of the DOB " + reset + "[dd]: ")
        term_list.append(day)
        year = input(red_bold + "Enter the year of the DOB " + reset + "[yyyy]: ")
        term_list.append(year)
        year_short = input(red_bold + "Enter the year of the DOB again " + reset + "[yy]: ")
        term_list.append(year_short)
    else:
        pass
    # Check for phone number area code
    area_code = input(red_bold + "Do you know the targets phone number? " + reset + "[y/n] ")
    if area_code == "y":
        ac_answ = input(red_bold + "Enter the area code of the phone number: " + reset + "[###] ")
        term_list.append(ac_answ)
    else:
        pass
    # Check for favorite sports team
    sports_team = input(red_bold + "Do you know the targets favorite sports team? " + reset + "[y/n] ")
    if sports_team == "y":
        st_answ = input(red_bold + "Enter the team: " + reset)
        term_list.append(st_answ)
    else:
        pass
    print(red_bold + "The terms you entered are: " + reset, term_list)
    # Check for more terms
    more_terms = input(red_bold + "Are there any other terms you want to add? " + reset + "[y/n] ")
    if more_terms == "y":
        n = int(input(red_bold + "Enter the number of terms: " + reset))
        for i in range(0, n):
            print(red_bold + "Enter term number {}: ".format(i + 1) + reset)
            # Add the element to the list
            term_list.append(input())
    else:
        pass
    print(red_bold + "The entered terms are: \n" + reset, term_list)
    follow_thru = input(red_bold + "Do you want to continue: " + reset + "[y/n] ")
    if follow_thru == "y":
        pass
    else: 
        pass
    master_list += term_list


    # call other functions for use of term_list
    master_list = term_combine(term_list)
    # master_list += combined_list
    combined_list = master_list
    master_list += both_cap(term_list)
    combined_list = master_list
    for symbol in ['!', '_', '%', "$", "@", ".", "-", "*", "&"]:
        master_list += sep_word(term_list, symbol)
    combined_list = master_list
    for old_value, new_value in [("a", "@"), ("s", "$"), ("e", "3"), ("o", "0"), ("l", "1"), ("r", "4"), ("i", "1")]:
        master_list += change_char(old_value, new_value, combined_list)
    combined_list = master_list
    for sym in ["!", "$", "@", "&", "."]:
        master_list += end_sym(sym, combined_list)
    # Open a file for writing to and create on if it doesnt exist
    f = open(file_name, "w+")
    # Write the data to the file
    for elem in set(master_list):
        if len(elem) >= 8:
            f.write(elem + "\n")
    # Close the file when done
    f.close()


# Create function that takes in master list and combines elements together
def term_combine(master_list):
    master_copy = []
    master_copy = list(''.join(entry) for entry in itertools.product(master_list, repeat=2))
    return master_copy

# Create a function that caps both words
def both_cap(term_list):
    cap_both_list = []
    for elem in term_list:
        cap_both_list.append(elem.capitalize())
    cap_both_list = list(''.join(entry) for entry in itertools.product(cap_both_list, repeat=2))
    return cap_both_list

# Create a function that caps the second word in the list
# def cap2(term_list):
#     term_list_copy = term_list.copy()
#     cap2_list = []
#     for elem in term_list_copy:
#         cap2_list.append(elem.capitalize())
#     cap2_list = list(''.join(entry)
#         for entry in itertools.product(cap2_list, repeat=2))

#     print(cap2_list)

# Create a list that takes in combine_list a caps the first letter of the element
def cap_char1():
    cap1_list = []
    for elem in master_list:
        cap1_list.append(elem.capitalize())
    return cap1_list

# Shorten into on function with a tuple and for loop
def sep_word(term_list, value):
    sep_list = []
    sep_list = list(value.join(entry) for entry in itertools.product(term_list, repeat=2))
    return sep_list

# Shorten into on function with a tuple and for loop
def change_char(old_value, new_value, master_list):
    new_list = master_list.copy()
    for idx, value in enumerate(new_list):
        new_list[idx] = value.replace(old_value, new_value)
    return new_list

# Create a function that adds syms to end
def end_sym(value, master_list):
    new_list = []
    for elem in master_list:
        new_elem = elem + value
        new_list.append(new_elem)
    return new_list 

# Create a function that adds the a number 0-9 to the end

# combine all the lists togehter into one big list

# Create a new list that caps the first letter in the elements of the list

# Combine the lists again

# Go through that final list and get rid of and element that has less than 6 charaters in it.

# Go through the list and get rid of duplicates

# # output that list onto a file as a wordlist


def main():
    usr_input()

if __name__ == "__main__":
    main()
