#rotate an array by a number to the right

array = [1,2,3,4,5]

rot = []

number = 2
index = 2

for i in range(index + 1 , 5):
    rot.append(array[i])

for _ in range(index + 1):
    rot.append(array[_])

print(rot)
