def add(num):
    if num == 0:
        return num
    else:
        return add(num-1) + num
    

a=int(input("enter the number"))

print(add(a))
