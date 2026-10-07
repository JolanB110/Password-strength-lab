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


Simple_brute_force("abc")