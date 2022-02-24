import sys
import os

# check the version of python that the user is using. is older than version 3, print an error message.
if sys.version_info < 3:
    raise Exception("Sorry, Operation Project Hackerman only works with Python 3 ")

