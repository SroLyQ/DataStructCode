x=[]
while True:
    a=int(input())
    if a==0 :
      break
    x.append(a)
a=str(input()).lower()
if 'n' in a:
    x.sort()
else :
    x.sort(reverse = True)
for w in x:
    print(w,end=" ")
