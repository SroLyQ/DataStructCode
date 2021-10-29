print("*** Fun with countdown ***")
x=list(map(int, input('Enter List : ').split(' ')))
y=[]
ans=0
ansl=[]
for i in range(len(x)):
    if(x[i]==1):
        z=[]
        z.append(x[i])
        j=i
        while(x[j-1]==x[j]+1):
            z.append(x[j-1])
            j-=1
        z.reverse()
        y.append(z)
        ans+=1
ansl.append(y)
ansl.insert(0,ans)
print(ansl)