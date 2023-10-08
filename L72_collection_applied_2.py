menuList = []
def showBill():
    total_p = 0
    print("My Food".center(len("My Food")+10,"+"))
    for number in menuList:
        print(number[0], "=", number[1], "บาท")
        total_p += float(number[1])
    print("Total:", total_p, "บาท")

while True:
    menuN = input("Please Enter Menu: ")
    if menuN.lower() == "e":
        break
    else:
        menuP = input("Enter Price: ")
        menuList.append([menuN, menuP])

showBill()

print("=========================")
print(menuList)

