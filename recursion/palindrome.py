str1 = str(input("enter a string"))

def palindrome(l,r):
    if l == r:
        return True
    if str1[l] != str1[r]:
        return False
    return palindrome(l+1,r-1)

print(palindrome(0,len(str1)-1))