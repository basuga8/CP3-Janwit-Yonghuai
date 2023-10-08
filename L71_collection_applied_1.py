menu_list = []
price_list = []

def show_bill():
    print("===food===")
    while True:
        menu_N = input("Please Enter Menu: ")
        if menu_N.lower() == "ex":
            break
        else:
            menu_P = int(input("Price: "))
            menu_list.append(menu_N)
            price_list.append(menu_P)
    print("BILL".center(len("BILL") + 20, "+"))
    for i in range(len(menu_list)):
        print(menu_list[i], "=", price_list[i], "บาท")
    print("Total".center(len("Total") + 20, "+"))
    print("รวมเป็นเงิน", sum(price_list), "บาท")

show_bill()


