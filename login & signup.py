"""cybernetics project"""

# header design
design = "☻"
print(design.center(119, "*"))
title = "♦DRSHIELD v0.2♦"
print(title.center(119, "*"))
org = "♦TEAM KIT♦"
print(org.center(119, "*"))
print(design.center(119, "*"))

# variables to store login details in list form
users = ["test"]
pin = ["1234"]


# function declaration
def log():
    # login function.match login details
    uid = input("\nUSERNAME: ")
    pas = input("PIN: ")

    un = users.count(uid)
    pn = pin.count(pas)
    index = users.index(uid)

    if un == 1 and pn >= 1:
        if pas == pin[index]:
            return 0
        else:
            return 1
    else:
        return 2


def sig():
    # signup function.create new user
    newuid = input("\nENTER YOUR USERNAME: ")
    newpd = input("ENTER YOUR PIN: ")
    cid = users.count(newuid)
    if newpd.isnumeric():
        if len(newpd) == 4:
            if cid == 0:
                pin.append(newpd)
                users.append(newuid)
                return 0
            else:
                return 1
        else:
            return 2
    else:
        return 3


def show_list():
    # secret function to how all login detail
    print(users)
    print(pin)


# recursive loop for presentation layer
while True:
    # exception handling
    try:
        # login process
        login = int(input("\nENTER 1 TO LOG IN\nENTER 2 TO SIGN UP: "))
        if login == 1:
            for i in range(3):
                y = log()
                if y == 0:
                    print("\n♦☻♠WELCOME TO CYBER-WORLD♠☻♦")  # your code goes here!!!executed after login
                    break
                else:
                    print("\nTRY AGAIN!!!\nWRONG COMBINATION.")
                    if i == 2:
                        print("\nINVALID USER!!!")
                        break
        # signup process
        elif login == 2:
            for i in range(3):
                s = sig()
                if s == 0:
                    print("\nSIGNED-UP.\nLOG IN TO CONTINUE.")
                    break
                elif s == 1:
                    print("\nENTER UNIQUE CREDENTIALS.")
                    print("TRY AGAIN!!!")
                    if i == 2:
                        print("SESSION EXPIRED")
                        break
                elif s == 2:
                    print("\nPIN SHOULD BE IN FOUR DIGITS ONLY.")
                    print("TRY AGAIN!!!")
                    if i == 2:
                        print("SESSION EXPIRED")
                        break
                elif s == 3:
                    print("\nPIN SHOULD BE NUMERIC.")
                    print("TRY AGAIN!!!")
                    if i == 2:
                        print("SESSION EXPIRED")
                        break
        # secret key for secret function
        elif login == 5214785478965896325632145:
            show_list()

        else:
            print("\nWRONG INPUT")
    except Exception as err:
        print("ERROR FOUND", err)

    while True:

        a = input("\nIF YOU WANT TO CONTINUE PRESS Y/N:  ")
        if a in ("y", "n"):
            break
    if a == "y":
        continue
    else:
        print("\nTHANK YOU WE HOPE YOU'LL VISIT US AGAIN")
        break
