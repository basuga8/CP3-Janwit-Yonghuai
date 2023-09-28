numm = 5
for row in range(1,numm+1):
    for column in range(1):
        column = " " * (numm-row)
    for x in range(1):
        x = 2 * row - 1
    print(column + ("*" * x))

print("========================================")

# ย่อได้อีก
num = int(input())
for y in range(num):
    print(" "*(num-y),"*"*((y*2)+1))