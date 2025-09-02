#Given a number N and a number K get the last digit when the number N is raised to the power of K
#the numbers can be very big

N =int(input("enter the number"))

K =int(input("enter the power to be raised to"))

a = N ** K

print(a%10)


