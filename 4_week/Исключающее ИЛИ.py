def xor(x, y):
    if (x == 1 and y == 0) or (y == 1 and x == 0):
        return 1
    elif (x == 0 and y == 0) or (x == 1 and y == 1):
        return 0

x = int(input())
y = int(input())
print(xor(x, y))
