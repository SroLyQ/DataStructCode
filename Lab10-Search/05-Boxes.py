inp1,n = input('Enter Input : ').split('/')
inp1 = [int(e) for e in inp1.split()]
data=inp1.copy()
inp1.sort(reverse=True)
n=int(n)
l=inp1[0]
r=100
while(l!=r):
    mid=int((l+r)/2)
    box=[]
    alrShift=False
    for i in range(n):
        box.append(mid)
    j=0
    for i in data:
        while( j < n and box[j]<i):
           j+=1
        if j >= n:
            l=mid+1
            alrShift=True
            break
        box[j]-=i
    if not alrShift:
        r=mid

print('Minimum weigth for {0} box(es) = {1}'.format(n,l))
