#this question was asked in the power coding round of virtusa
#idr the exact question but the input is TWO INTEGERS convert the first integer to binary , flip every digit 0-1 , 1-0 , and check the divisibility with the second number
#flip only one digit at a time 
#the number will not be greater than 32 bit

N1 = int(input("enter the first number (to be converted to binary)"))
N2 = int(input("divisibility number"))

numb = bin(N1)

n=len(numb)

inum = N1
x = n-2
print(numb)

for i in range (n-1,1,-1):
    inum = N1
    if numb[i]=='0':
        inum = inum + 2 ** ((n-1)-i)
        print ("added")
    else:
        inum = inum - 2 ** ((n-1)-i)
        print("subtracted")
    if inum % N2 == 0:
        print(inum, "is divisble")
        print((n-1)-i,"th digit")
        break    

       
  


