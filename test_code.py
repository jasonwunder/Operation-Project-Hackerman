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

# Create a function for the user provied terms


def usr_input():
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
    print("The terms you entered are: ", term_list)
    # Check for more terms
    more_terms = input("Are there any other terms you want to add? [y/n]")
    if more_terms == "y":
        n = int(input("Enter the number of terms: "))
        for i in range(0, n):
            print("Enter term number {}: ".format(i + 1))
            # Add the element to the list
            term_list.append(input())
        return term_list
    print("The entered terms are: \n",term_list)

# Create function that takes in master list and combines elements together 
def term_combine():
    list = usr_input()
    for element in list:
        print(element)

term_combine()


# Have user validate if information is correct. If it is not have them enter the terms again.

# create a function that looks for date formats within the list

# Create a password generator that intergrates the list that was created by the user.


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
