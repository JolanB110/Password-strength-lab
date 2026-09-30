
pswd = input("Enter your password: ")

#define characteristics of a strong password

caracteristics = {
    "length": 8,
    "uppercase": 1,
    "lowercase": 1,
    "digits": 1,
    "special": 1,
    "personal_info": 0
}

#these characteristics can be modified to fit the user's needs. The default values are set to encourage a strong password.


def character_repetition(c, characters, penalty):
    if len(characters) > 1 and c == characters[-2]:
        penalty += 0.5

    return penalty


def pattern_repetition(password):
    penalty = 0

    #a pattern must contain at least 2 characters
    for pattern_length in range(2, len(password) // 2 + 1):

        pattern = password[:pattern_length]

        #check whether the whole password is made of this pattern
        repetitions = len(password) // pattern_length

        if repetitions >= 2 and pattern * repetitions == password:
            penalty += (repetitions - 1) * 0.5
            break

    return penalty


def check_password_strength(password, caracteristics):
    cursor = 0
    penalty = 0
    characters = []

    #check consecutive character repetitions
    for i in password:
        characters.append(i)
        penalty = character_repetition(i, characters, penalty)

    #check repeated patterns
    penalty += pattern_repetition(password)

    cursor -= penalty

    return cursor


check = check_password_strength(pswd, caracteristics)

print(f"Your password strength score is: {check}/9")

