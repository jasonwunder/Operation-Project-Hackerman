import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!#$%&()*+,-./:;<=>?@[\\]^_`{|}~"

upper = True
lower = True
numbers = True
syms = True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if numbers:
    all += digits
if syms:
    all += symbols

length = 15
amount = 10

for passwd in range(amount):
    password = "".join(random.sample(all, length))
    print(password)

