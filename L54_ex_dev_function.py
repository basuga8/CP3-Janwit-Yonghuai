def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Success !")
        menu()
    else:
        print("Failed !!")
        login()
#--------------------------------------------------------------
def menu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print(select())
#--------------------------------------------------------------
def select():
    userSelected = int(input("Select Number: "))
    if userSelected == 1:
        return vat(total = int(input("Price (THB) : ")))
    elif userSelected == 2:
        return pr()
    else:
        print(select)
# --------------------------------------------------------------
def vat(total):
    #price = int(input("Price (THB) : "))
    vat = 7
    result = total + (total * vat / 100)
    return "Total + v.7% : "+ str(result)+ " บาท"
#--------------------------------------------------------------
def pr():
    price1 = int(input("First Price : "))
    price2 = int(input("Second Price : "))
    total = price1 + price2
    print("Total: บาท ", total)
    return vat(total)

login()