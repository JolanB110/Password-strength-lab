from itertools import product

#List of characters to use for brute force
char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z',
             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
             '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',
             ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
             '`', '~',]

#Simple brute force function to find a password.
def Simple_brute_force(password):
    iteration = 0
    length = 1

    #while loop to keep trying until the password is found
    while True:

        #Generate every possible combination for the current password length
        for combination in product(char_list, repeat=length):
            forcedPassword = ''.join(combination)
            iteration += 1

            #print(f"Trying password: {forcedPassword}")

            if forcedPassword == password:
                print("Result of Simple Brute Force:")
                print(f"Password found: {forcedPassword}")
                print(f"Number of attempts: {iteration}")
                return

        #Increase the password length if the password was not found
        length += 1

Simple_brute_force(input("Enter the password to brute force: ") or "abc")


"""
ideal brute force function to find a password much easier than
the simple brute force function. This function will check every character
in the password and will validate characters one by one instead of
checking every possible combination.
"""

def Ideal_brute_force(password):
    iteration = 0
    forcedPassword = ""

    #Check every character in the password one by one
    for i in range(len(password)):

        #try every character from the character list
        for char in char_list:
            iteration += 1

            #print(f"Trying character: {char}")

            if char == password[i]:
                forcedPassword += char
                break

    if forcedPassword == password:
        print("Result of Ideal Brute Force:")
        print(f"Password found: {forcedPassword}")
        print(f"Number of attempts: {iteration}")
        return

"""
WARNING : This will not work in real use because you can't check the password
character by character. This is just a simulation of how it would work if
you could check the password character by character.
"""

Ideal_brute_force(input("Enter the password to brute force: ") or "abc")


"""
Dictionary brute force function to find a password faster than simple brute force.
This function will use a dictionary of common passwords to check against first
before trying every possible combination.
"""

def Dictionary_brute_force(password):
    iteration = 0

    with open("data/french_passwords_top20000.txt", "r") as file:
        for line in file:
            iteration += 1
            forcedPassword = line.strip()

            #print(f"Trying password: {forcedPassword}")

            if forcedPassword == password:
                print("Result of Dictionary Brute Force:")
                print(f"Password found: {forcedPassword}")
                print(f"Number of attempts: {iteration}")
                return

    #if the password was not found in the dictionary, use simple brute force
    print("Password not found in dictionary, using simple brute force...")
    if input("Do you want to continue using simple brute force ? (y/n): ").lower() == "y":
        Simple_brute_force(password)

Dictionary_brute_force(input("Enter the password to brute force: ") or "abc")