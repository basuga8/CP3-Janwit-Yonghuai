input = 5
for row in range(1,input+1):
    for column in range(1):
        column = " " * (input-row)
    for x in range(1):
        x = (2 * row - 1)
    print(column + ("*" * x))
