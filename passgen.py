import random
def letterChange(passToChange): # replaces certain numbers with symbols
    if 'i' in passToChange:
        passToChange = passToChange.replace(passToChange[passToChange.lower().find('i')], "1")

    if 'a' in passToChange:
        passToChange = passToChange.replace(passToChange[passToChange.lower().find('a')], "@")

    if 'o' in passToChange:
        passToChange = passToChange.replace(passToChange[passToChange.lower().find('o')], "0")

    if 's' in passToChange:
        passToChange = passToChange.replace(passToChange[passToChange.lower().find('s')], "$")

    if 'h' in passToChange:
        passToChange = passToChange.replace(passToChange[passToChange.lower().find('h')], "#")

    return passToChange

check = True
# checks that phrases are greater than 3 in length
while check:
    # asks users for 3 phrases
    passphrase1 = input("Enter the first phrase: ")
    if len(passphrase1) <= 3:
        print("phrase needs to be greater than 3 letters")
    else:
        passphrase2 = input("Enter the second phrase: ")
        if len(passphrase2) <= 3:
            print("phrase needs to be greater than 3 letters")
        else:
            passphrase3 = input("Enter the third phrase: ")
            if len(passphrase3) <= 3:
                print("phrase needs to be greater than 3 letters")
            else:
                check = False # exits

# choices a random number to select a letter at that index number
randNum1 = random.randint(0,(len(passphrase1) - 1))
randNum2 = random.randint(0,(len(passphrase2) - 1))
randNum3 = random.randint(0,(len(passphrase3) - 1))

# uses the random number as an index in the string and changes the letter at that index uppercase
pass1 = passphrase1.replace(passphrase1[randNum1], passphrase1[randNum1].upper(), 1)
pass2 = passphrase2.replace(passphrase2[randNum2], passphrase2[randNum2].upper(), 1)
pass3 = passphrase3.replace(passphrase3[randNum3], passphrase3[randNum3].upper(), 1)

# uses letterChange function to change certain numbers  
finalPass1 = letterChange(pass1)
finalPass2 = letterChange(pass2)
finalPass3 = letterChange(pass3)

print("Your new password is: " + finalPass1 + "_" + finalPass2 + "_" + finalPass3) # new password is generated