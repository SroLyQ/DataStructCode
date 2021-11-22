def bi_search(l, r, arr, x):
    mid = int((l+r)/2)
    if l==r:
        if arr[r] == x:
            return True
        else:
            return False
    if(arr[mid]>=x):
        r=mid
    elif arr[mid]<x:
        l=mid+1
    return bi_search(l,r,arr,x)

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))