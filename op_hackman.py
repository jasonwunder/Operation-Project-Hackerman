#! /usr/bin/python
from doctest import master
import sys
import os
import random
import itertools
from typing import final

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
master_list = []

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
    for elem in term_list:
        master_list.append(elem)
    # call other functions for use of term_list
    term_combine()
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
    change_char("a", "@")
    change_char("s", "$")
    change_char("e", "3")
    change_char("o", "0")
    change_char("b", "9")
    change_char("l", "1")
    change_char("r", "4")
    change_char("t", "7")
    change_char("i", "1")
    end_sym("!")
    end_sym("$")
    end_sym("@")
    end_sym("*")
    end_sym("&")
    end_sym(".")
# Create function that takes in master list and combines elements together
def term_combine():
    master_copy = []
    master_copy = list(''.join(entry)
                       for entry in itertools.product(master_list, repeat=2))
    for elem in master_copy:
        master_list.append(elem)
    return master_list

# Create a function that caps both words
def both_cap(term_list):
    cap_both_list = []
    for elem in term_list:
        cap_both_list.append(elem.capitalize())
    cap_both_list = list(''.join(entry)
                         for entry in itertools.product(cap_both_list, repeat=2))
    for elem in cap_both_list:
        master_list.append(elem)
    return master_list

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
    for elem in cap1_list:
        master_list.append(elem)
    return master_list

# Shorten into on function with a tuple and for loop
def sep_word(term_list, value):
    sep_list = []
    sep_list = list(value.join(entry)
                    for entry in itertools.product(term_list, repeat=2))
    for elem in sep_list:
        master_list.append(elem)
    return master_list

# Shorten into on function with a tuple and for loop
def change_char(old_value, new_value):
    new_list = master_list.copy()
    for idx, value in enumerate(new_list):
        new_list[idx] = value.replace(old_value, new_value)
    for elem in new_list:
        master_list.append(elem)
    return master_list

# Create a function that adds syms to end
def end_sym(value):
    new_list = master_list.copy()
    for elem in new_list:
        new_elem = elem + value
    master_list.append(new_elem)
    return master_list

# Create a function that adds the a number 0-9 to the end

# combine all the lists togehter into one big list

# Create a new list that caps the first letter in the elements of the list

# Combine the lists again

# Go through that final list and get rid of and element that has less than 6 charaters in it.

# Go through the list and get rid of duplicates

# # output that list onto a file as a wordlist
# def main():
#     # Open a file for writing to and create on if it doesnt exist
#     f = open("test_file.txt", "w+")
#     # Write the data to the file
#     for elem in master_list:
#         print(elem, file = f)
#     # Close the file when done
#     f.close()

# if __name__ == "__main__":
#     main()


# -_-_-_-_-_-_-_-_-_-_-_-_- TEST CODE -_-_-_-_-_-_-_-_-_-_-_-_-_-
usr_input()
# print(master_list)
# for elem in master_list:
#     print(elem)
print(len(master_list))


