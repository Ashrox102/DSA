def bsearch(arr,l,r,num):
    if l>r:
        return -1
    mid = (l+r)//2
    
    if arr[mid] == num:
        return mid
    
    if arr[mid] > num:
        return bsearch(arr,l,mid-1,num)
    else:
        return bsearch(arr,mid+1,r,num)
    

arr = [1,2,3,4,5,8,9,10]

print(bsearch(arr,0,len(arr)-1,8))

