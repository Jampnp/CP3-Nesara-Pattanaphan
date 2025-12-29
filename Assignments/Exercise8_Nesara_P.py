usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "admin" and passwordInput == "1234":
    print("Welcome !!")
    print("Paper    120 THB/each")
    print("Pencil   20  THB/each")
    print("Notebook 45  THB/each")
    productName = input("What do you want to buy? :")
    numberOfProduct = int(input("How many ? :"))
    if productName == "Paper":
        print("Price =",numberOfProduct*120,"THB")
    elif productName == "Pencil":
        print("Price =",numberOfProduct*20,"THB")
    elif productName == "Notebook":
        print("Price =",numberOfProduct*45,"THB")
    print("Thank you")
else:
    print("Wrong username or password.")