#rotate an array by a number to the right

array = [1,2,3,4,5]

rot = []

number = 2
index = 2

for i in range(index + 1 , 5):
    print(i)
    rot.append(array[i])

for _ in range(index):
    rot.append(_)

print(rot)
