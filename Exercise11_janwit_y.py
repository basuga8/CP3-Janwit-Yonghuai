numm = int(input("ใส่ตัวเลข: "))
for row in range(1,numm+1):
    for column in range(1):
        column = " " * (numm-row)
    for x in range(1):
        x = 2 * row - 1
    print(column + ("*" * x))
