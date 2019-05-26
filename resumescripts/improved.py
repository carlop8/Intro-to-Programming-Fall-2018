#Carlisaac Nicolas
#10/2/2018
#This program sets up user ID and password


def createuserid():
    fname=(input("Good Day. Write first name.").lower())
    lname= (input("Write last name.").lower())
    global userid
    userid=fname[0]+lname
    print("Your user ID is",userid)
    return userid


def checkcharacter():
    global passw
    passw = input("Input a password with the first character as a capital letter and is more than 6 characters long.")
    while (64 >= ord(passw[0])) or (91 <= ord(passw[0])):
        passw = input("Password must have capital in first character. Enter new password.")
    return passw


def checkrest():
    global passw
    for i in passw:
        while len(passw) < 6:
            passw = input("Password is too short enter a new one.")
    if checkcharacter() is False:
        createpassword()
    else:
        print("Your password is ", passw, "Thank You.")


def createpassword():

    checkcharacter()
    checkrest()
    input('Enter')


def main():
    createuserid()
    print(userid)
    createpassword()


main()