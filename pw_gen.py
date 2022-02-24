import random

# set the variables on what is included in the passwords
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!#$%&()*+,-./:;<=>?@[\\]^_`{|}~"

# set the booleans for the password rules 
upper = True
lower = True
numbers = True
syms = True

# create a string containing all the you will use
all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if numbers:
    all += digits
if syms:
    all += symbols

# set the length of the passwords and the amount of passwords to be generated
length = 25
amount = 10

# join the all string with a empty string to create the passwords. then print the new variable
for passwd in range(amount):
    password = "".join(random.sample(all, length))
    print(password)

