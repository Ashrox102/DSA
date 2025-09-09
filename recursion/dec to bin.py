def conv(dec):
    if dec < 2:
        return str(dec)
    return conv(dec//2) + str(dec%2)

a = int(input("enter the decimal number"))

print(conv(a))