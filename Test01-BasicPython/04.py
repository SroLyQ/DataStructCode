print('*** String Rotation ***')
lSt,rSt=input('Enter 2 strings : ').split(' ')
lSt=list(lSt)
rSt=list(rSt)
tempL=lSt.copy()
tempR=rSt.copy()
r = 1
i=0
tempStrL=''
tempStrR=''
ch=False
for i in range(0,len(tempL)):
    tempL[i]=lSt[(i-2)%len(tempL)]
for i in range(0,len(tempR)):
    tempR[i]=rSt[(i+3)%len(tempR)]
for i in range(0,len(tempL)):
    tempStrL += tempL[i]
for i in range(0,len(tempR)):
    tempStrR += tempR[i]
print('1 ' + tempStrL+' '+tempStrR)
while(tempL != lSt or tempR != rSt):
    r+=1
    tempStrL=''
    tempStrR=''
    lisL=tempL.copy()
    lisR=tempR.copy()
    for i in range(0,len(tempL)):
        tempL[i]=lisL[(i-2)%len(tempL)]
    for i in range(0,len(tempR)):
        tempR[i]=lisR[(i+3)%len(tempR)]
    for i in range(0,len(tempL)):
        tempStrL += tempL[i]
    for i in range(0,len(tempR)):
        tempStrR += tempR[i]
    if(r<=5):
        print(str(r)+' '+ tempStrL + ' '+tempStrR)
    if(r==6):
        print(' . . . . . ')
        ch=True
if ch:
    print(str(r)+' '+ tempStrL + ' '+tempStrR)
print('Total of  ' + str(r) +' rounds.')
#while(tempL != lSt or tempR != rSt):