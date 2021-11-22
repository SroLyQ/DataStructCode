def findUpperBound(l,r,arr,x):
    mid = int((l+r)/2)
    if l==r:
        if r == len(arr)-1:
            return 'No First Greater Value'
        else:
            return str(arr[mid])
    if arr[mid] <= x:
        l = mid+1
    elif arr[mid] > x :
        r = mid
    return findUpperBound(l,r,arr,x)
inp1,inp2=input('Enter Input : ').split('/')
inp1=[int(e) for e in inp1.split()]
inp2=[int(e) for e in inp2.split()]
for i in inp2:
    print(findUpperBound(0,len(inp1)-1,sorted(inp1),i))