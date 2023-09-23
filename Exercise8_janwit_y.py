print("==============================")
print("=========WELL COME TO=========")
print("=== ***Lung_Lang_Shoppp*** ===")
print("=======____[Log in]____=======")

username = input("Username : ")
password = input("Password : ")

if username == "devzaa" and password == "1212":
    print("*** Log in Success ***")
    print(">>>>>>>รายการสินค้าทั้งหมด<<<<<<<")
    IP = "1. iPhon 70 Pro Maxxx        = 73900 บาท"
    SS = "2. Samsung Z Fold 80 Ultra   = 69900 บาท"
    HW = "3. Huawei Mate 999 Pro       = 65800 บาท"
    OP = "4. OPPO Flip 500G            = 42000 บาท"
    NK = "5. Nokia 3311                =  3300 บาท"
    ip = float(73900)
    ss = float(69900)
    hw = float(65800)
    op = float(42000)
    nk = float(3300)
    end0 = "==================================="
    end1 = "!! ไม่มีรายการสินค้านี้ !!"
    end2 = ">>กรุณาระบุหมายเลขสินค้าอีกครั้ง<<"
    end3 = "==================================="

    print(IP)
    print(SS)
    print(HW)
    print(OP)
    print(NK)

    selected_n = (int(input("เลือกหมายเลขสินค้า: ")))
    if  selected_n > 5:
        print(end0)
        print(end1)
        print(end2)
        print(end3)
    elif selected_n == 0:
        print(end0)
        print(end1)
        print(end2)
        print(end3)
    else:
        if selected_n == 1:
            selected_n = ip
        elif selected_n == 2:
            selected_n = ss
        elif selected_n == 3:
            selected_n = hw
        elif selected_n == 4:
            selected_n = op
        elif selected_n == 5:
            selected_n = nk

        selected_p = int(input("เลือกจำนวนสินค้า: "))
        vat = 7
        cal_total = float(selected_n * selected_p)
        cal_vat = float((selected_n * 7 / 100) * selected_p)
        print("=================================================")
        print("=================================================")
        print("=================================================")
        if selected_n == ip:
            print(IP)
        elif selected_n == ss:
            print(SS)
        elif selected_n == hw:
            print(HW)
        elif selected_n == op:
            print(OP)
        elif selected_n == nk:
            print(NK)
        print("==จำนวน =", selected_p)
        print("==ราคาสินค้ารวม", selected_n * selected_p, "บาท")
        print("==vat.7% =", cal_vat, "บาท")
        print("ราคารวมสุทธิ =", cal_total + cal_vat, "บาท")
        print("=================================================")
        print("==================THANK_YOU======================")
        print("=================================================")

else:
    print("!!Log in Failed!!")