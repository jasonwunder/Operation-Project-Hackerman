#! /usr/bin/python
from doctest import master
import sys
import os
import random
import itertools
from tkinter.font import BOLD
from turtle import position
from typing import final
from tqdm import tqdm


print("""\
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
                    """)
# check the version of python that the user is using. if older than version 3, print an error message.
if (sys.version_info < (3, 5)):
    print('Error: Operation Project Hackerman only works with Python 3')
    sys.exit(1)
# Create a master list that every function will append to to make one big list


# class colors:
reset = '\033[0m'
bold = '\033[01m'
disable = '\033[02m'
underline = '\033[04m'
red = '\033[31m'
lightgreen = '\033[92m'
yellow = '\033[93m'

# bold_red = "\033[1;31;40m"
print(bold + "Welcome \nThis tool requires that you know some information about the target." + reset)
contin = input("Select yes to continue: [y/n] ")
if contin == "y":
    loop = tqdm(total=5000, position=0, leave=False)
    for k in range(5000):
        loop.set_description("Loading...".format(k))
        loop.update(1)
    loop.close()
# Create a function for the user provied terms
def usr_input():
    master_list = []
    file_name = input("Enter name for output file: ")
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
