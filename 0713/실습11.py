for x in range(2, 10):
    print(str(x) + "단")
    for y in range(1, 10):
        print(x, "x", y, "=", x * y)

for dan in range(2,10):
    print(str(dan) + "단")
    for i in range(1, 10):
        print(f'{dan} x {i} = {dan * i}')