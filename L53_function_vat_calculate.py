def vat_cal(price):
    result = price + (price * (7/100))
    return "คุณต้องจ่ายเงินทั้งสิ้น ="+ str(result)
print(vat_cal(int(input("ใส่ราคาสิ้นค้า = "))))
