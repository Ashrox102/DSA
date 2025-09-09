s = list(str(input("enter the string ")))

def rstring (l,r):
    if l<r:
        s[l],s[r] = s[r],s[l]
        return rstring(l+1,r-1)
rstring(0,len(s)-1)
print("".join(s))
                      