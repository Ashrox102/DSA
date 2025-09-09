def anagram(str2,str1,i):
    if i == 0:
        return True
    if str1[i] in str2:
        return anagram(str2,str1,i-1)
    else:
        return False
    
st1 = str(input("enter the first string")) 
st2 = str(input("enter the second string"))

print(anagram(st1,st2,len(st1)-1))