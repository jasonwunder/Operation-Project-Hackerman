###################################################################################################
############# THIS IS NOT FOR MAIN PRODUCT#################
###################################################################################################
from doctest import master
from email.utils import collapse_rfc2231_value
import sys
import os
import random
import itertools


# check the version of python that the user is using. if older than version 3, print an error message.
if (sys.version_info < (3, 5)):
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
    # underscore(term_list)
    # dot(term_list)
    # star(term_list)
    # explanation(term_list)
    # dollar(term_list)
    # at_sign(term_list)
    # minus_sign(term_list)
    # percent_sign(term_list)
    # carrot_sign(term_list)
    both_cap(term_list)
    # cap2(term_list)
    # a_change_at(term_list, "a", "@")
    # zero_change(term_list)
    # three_change(term_list)
    # dollar_sign(term_list)
    # nine_change(term_list)
    # one_change(term_list)
    # four_change(term_list)
    # one_i_change(term_list)
    # seven_change(term_list)
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
    # print(cap_both_list)

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
def cap_char1(combine_list):
    cap1_list = []
    for elem in combine_list:
        cap1_list.append(elem.capitalize())
    for elem in cap1_list:
        master_list.append(elem)
    # print(cap1_list)

# Shorten into on function with a tuple and for loop
def sep_word(term_list, value):
    sep_list = []
    sep_list = list(value.join(entry)
        for entry in itertools.product(term_list, repeat=2))
    for elem in sep_list:
        master_list.append(elem)
    

    

# Create a function that adds "_" between the two terms
# def underscore(term_list):
#     underscore_list = []
#     underscore_list = list('_'.join(entry)
#         for entry in itertools.product(term_list, repeat=2))
#     print(underscore_list)
# Create a function that adds "." between the two terms
# def dot(term_list):
#     dot_list = []
#     dot_list = list('.'.join(entry)
#         for entry in itertools.product(term_list, repeat=2))
#     print(dot_list)
# Create a function that adds a "*" between the two terms
# def star(term_list):
#     star_list = []
#     star_list = list('*'.join(entry)
#         for entry in itertools.product(term_list, repeat=2))
#     print(star_list)
# Create a function that adds a "!" between the two terms
# def explanation(term_list):
#     explanation_list = []
#     explanation_list = list('!'.join(entry)
#         for entry in itertools.product(term_list, repeat=2))
#     print(explanation_list)
# Create a function that adds a "$" between the two terms
# def dollar(term_list):
#     dollar_list = []
#     dollar_list = list('$'.join(entry)
#         for entry in itertools.product(term_list, repeat=2))
#     print(dollar_list)
# Create a function that adds a "@" between the two terms
# def at_sign(term_list):
#     at_sign_list = []
#     at_sign_list = list('@'.join(entry)
#         for entry in itertools.product(term_list, repeat=2))
#     print(at_sign_list)
# Create a function that adds a "-" between the two terms
# def minus_sign(term_list):
#     minus_sign_list = []
#     minus_sign_list = list('-'.join(entry)
#         for entry in itertools.product(term_list, repeat=2))
#     print(minus_sign_list)
# Create a function that adds a "%" between the two terms
# def percent_sign(term_list):
#     percent_sign_list = []
#     percent_sign_list = list('%'.join(entry)
#         for entry in itertools.product(term_list, repeat=2))
#     print(percent_sign_list)
# Create a function that adds a "^" between the two terms
# def carrot_sign(term_list):
#     carrot_sign_list = []
#     carrot_sign_list = list('^'.join(entry)
#         for entry in itertools.product(term_list, repeat=2))
#     print(carrot_sign_list)

# Shorten into on function with a tuple and for loop
def change_char(term_list, old_value, new_value):
    # new_char = [(old_value, new_value)]
    new_list = master_list.copy()
    change_char_list = []
    for idx, value in enumerate(new_list):
        new_list[idx] = value.replace(old_value, new_value)
        change_char_list.append(new_list[idx])
    for elem in change_char_list:
        master_list2.append(elem)
    # print(change_char_list)


# # Create a function that changes "a" to "@"
# def a_change_at(term_list, old_value, new_value):
#     new_list = term_list.copy()
#     for idx, value in enumerate(new_list):
#         new_list[idx] = value.replace(old_value, new_value)
#     print(new_list)
# # Create a function that changes "o" to "0"
# def zero_change(term_list):
#     zero_list = term_list.copy()
#     for idx, value in enumerate(zero_list):
#         zero_list[idx] = value.replace("o", "0")
#     print(zero_list)
# # Create a function that changes "e" to "3"
# def three_change(term_list):
#     three_list = term_list.copy()
#     for idx, value in enumerate(three_list):
#         three_list[idx] = value.replace("e", "3")
#     print(three_list)
# # Create a function that changes "s" to "$"
# def dollar_sign(term_list):
#     dollar_replace_list = term_list.copy()
#     for idx, value in enumerate(dollar_replace_list):
#         dollar_replace_list[idx] = value.replace("s", "$")
#     print(dollar_replace_list)
# # Create a function that changes "b" to "9"
# def nine_change(term_list):
#     nine_list = term_list.copy()
#     for idx, value in enumerate(nine_list):
#         nine_list[idx] = value.replace("b", "9")
#     print(nine_list)
# # Create a function that changes "l" to "1"
# def one_change(term_list):
#     one_list = term_list.copy()
#     for idx, value in enumerate(one_list):
#         one_list[idx] = value.replace("l", "1")
#     print(one_list)
# # Create a function that changes "r" to "4"
# def four_change(term_list):
#     four_list = term_list.copy()
#     for idx, value in enumerate(four_list):
#         four_list[idx] = value.replace("r", "4")
#     print(four_list)
# # Create a function that changes "i" to "1"
# def one_i_change(term_list):
#     one_i_list = term_list.copy()
#     for idx, value in enumerate(one_i_list):
#         one_i_list[idx] = value.replace("i", "1")
#     print(one_i_list)
# # Create a function that changes "t" to "7"
# def seven_change(term_list):
#     seven_list = term_list.copy()
#     for idx, value in enumerate(seven_list):
#         seven_list[idx] = value.replace("t", "7")
#     print(seven_list)
# Create a function that adds syms to end

# Create a function that adds a sym to begaining

# Create a function that adds the a number 0-9 to the end

# combine all the lists togehter into one big list

# Create a new list that caps the first letter in the elements of the list

# Combine the lists again

# Go through that final list and get rid of and element that has less than 6 charaters in it.
# for elem in final_list:
#     if len(elem) < 6:
#         delete elem
#     return final_list
# output that list onto a file as a wordlist


#-_-_-_-_-_-_-_-_-_-_-_-_- TEST CODE -_-_-_-_-_-_-_-_-_-_-_-_-_-
usr_input()
print(master_list)

for elem in master_list2:
    print(elem)
print(len(master_list))
print(len(master_list2))






































'''
#NOTES*******
###################################################################################### 

 number_list = []
    for num in range(0,100):
        number_list.append(num)
    random_number = random.choice(number_list)
    password_generated_list.append(str(random_number))

####################################################################################


    # maximum length of password needed
# this can be changed to suit your password length
MAX_LEN = 12
 
# declare arrays of the character that we need in out password
# Represented as chars to enable easy string concatenation
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
 
# combines all the character arrays above to form one array
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
 
# randomly select at least one character from each character set above
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
 
# combine the character randomly selected above
# at this stage, the password contains only 4 characters but
# we want a 12-character password
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
 
 
# now that we are sure we have at least one character from each
# set of characters, we fill the rest of
# the password length by selecting randomly from the combined
# list of character above.
for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
 
    # convert temporary password into array and shuffle to
    # prevent it from having a consistent pattern
    # where the beginning of the password is predictable
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
 
# traverse the temporary password array and append the chars
# to form the password
password = ""
for x in temp_pass_list:
        password = password + x
         
# print out password
print(password)
    
#######################################################################

#cap every other letter#
def mock(s):
    res = ""
    i = True
    for char in s:
        if i:
            res += char.upper()
        else:
            res += char.lower()
        i = not i
    return res


print(mock("Hello word program"))
'''
