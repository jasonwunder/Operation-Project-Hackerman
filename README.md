
![](https://raw.githubusercontent.com/jasonwunder/Operation-Project-Hackerman/main/images/op_hack_man.png)
#
# Table of contents
- [Why it was created](#why-is-was-created) 
- [How it Works](#how-it-works)
    - [File creation](#file-creation)
    - [Creating terms](#creating-terms)
    - [After the file is created](#after-the-file-is-created)
- [Requirements](#requirements)

#

Operation Project Hackerman is a unique tool to be used with password cracking tools. It takes in user input about the target by asking for specific information and also allowing the user to add more information. The tool will then provide thousands of combinations of those terms and create a word list for the user.

#

## Why is was created
Operation Project Hackerman was created to work with a brute force password attack, specifically against SSH. Having a custom-curated word list of potential passwords fills an empty void in recon. The standard terms that the user is asked to enter are the most common terms that non-technical/non-security oriented individuals will use in their passwords. 


![](https://raw.githubusercontent.com/jasonwunder/Operation-Project-Hackerman/main/images/one%20-%20Copy.PNG)

#

## How it works
### File creation
The user will be promted to create the name that they would like the word list file to be named.

![](https://raw.githubusercontent.com/jasonwunder/Operation-Project-Hackerman/main/images/two.PNG)

#

### Creating terms
The user will be asked a series of questions about the target which include:
- First name
- Middle name
- Last name
- Nickname
- Pets name
- Date of birth
- Phone number area code
- Favorite sports team

![](https://raw.githubusercontent.com/jasonwunder/Operation-Project-Hackerman/main/images/three.PNG)

The user will then have the chance to add any additional terms that they may have found during reconnaissance or any OSINT search.

![](https://raw.githubusercontent.com/jasonwunder/Operation-Project-Hackerman/main/images/four.PNG)

#

### After the file is created
Once the terms are selected and confirmed by the user, the tool will then create a word list file containing the terms that were entered. The file will have thousands of combinations of the words that include the most common character swaps and symbols. 

![](https://raw.githubusercontent.com/jasonwunder/Operation-Project-Hackerman/main/images/five.PNG)

The user will then be able to use a tool such as hydra, to perform a brute force attack against the target.

#

## Requirements 
In order to use this tool you must have tqdm installed
### How to install tqdm
In command line run the following command
```sh
pip instal tqdm
```
