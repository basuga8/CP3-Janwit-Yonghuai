systemMenu = {"ข้าวมันไก่" : 40, "ข้าวมันไก่พิเศษ" : 45, "ข้าวมันไก่ทอด" : 45, "ข้าวมันไก่รวม" : 50}

menuList = []
def showBill():
    print("===My Food===")
    print("----------------------------")
    total = 0
    for i in range(len(menuList)):
        print(menuList[i][0], "=", menuList[i][1], "บาท")
        total += int(menuList[i][1])
    print("----------------------------")
    print("รวมเป็นเงิน =", total, "บาท")
    print("----------------------------")

while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == "e":
        break
    elif menuName in systemMenu:
        menuList.append([menuName,systemMenu[menuName]])
    else:
        print("ไม่มีรายการ")

showBill()