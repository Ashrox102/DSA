def counting(num):
    if(num == 0):
        return
    counting(num-1)
    print("step number", num)

counting(50)
