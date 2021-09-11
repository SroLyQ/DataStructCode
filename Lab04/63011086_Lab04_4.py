class Queue:
    def __init__(self):
        self.queue=[]
    def __str__(self):
        return str(self.queue)
    def size(self):
        return int(len(self.queue))
    def pop(self):
        if(len(self.queue)>0):
            return self.queue.pop(0)
    def front(self):
        if(len(self.queue)>0):
            return self.queue[0]   
        return None
    def push(self,arg):
        self.queue.append(arg)
    def isEmpty(self):
        if(len(self.queue)>0):
            return False
        else:
            return True
inp = input('Enter Input : ').split(',')
myQ = Queue()
herQ = Queue()
for a in inp:
    a=a.split(' ')
    myQ.push(a[0])
    herQ.push(a[1])
myAct = Queue()
herAct = Queue()
print('My   Queue = ',end='')
while(not myQ.isEmpty()):
    temp=''
    a=myQ.pop()
    if(myQ.size()==0):
        print(a)
    else:
        print(a,end=', ');
    a=a.split(':')
    if a[0] == '0' :
        temp+='Eat:'
    elif a[0] == '1':
        temp+='Game:'
    elif a[0] == '2':
        temp+='Learn:'
    elif a[0] == '3':
        temp+='Movie:'
    if a[1] == '0':
        temp+='Res.'
    elif a[1]=='1':
        temp+='ClassR.'
    elif a[1]=='2':
        temp+='SuperM.'
    elif a[1]=='3':
        temp+='Home'
    myAct.push(temp)
print('Your Queue = ',end='')
while(not herQ.isEmpty()):
    temp=''
    a=herQ.pop()
    if(herQ.size()==0):
        print(a)
    else:
        print(a,end=', ');
    a=a.split(':')
    if a[0] == '0' :
        temp+='Eat:'
    elif a[0] == '1':
        temp+='Game:'
    elif a[0] == '2':
        temp+='Learn:'
    elif a[0] == '3':
        temp+='Movie:'
    if a[1] == '0':
        temp+='Res.'
    elif a[1]=='1':
        temp+='ClassR.'
    elif a[1]=='2':
        temp+='SuperM.'
    elif a[1]=='3':
        temp+='Home'
    herAct.push(temp)
score=0
myPrintTemp=[]
herPrintTemp=[]
while(not myAct.isEmpty()):
    myTemp=myAct.pop()
    myPrintTemp.append(myTemp)
    myTemp=myTemp.split(':')
    herTemp=herAct.pop()
    herPrintTemp.append(herTemp)
    herTemp=herTemp.split(':')
    if((myTemp[0] == herTemp[0]) and(myTemp[1] == herTemp[1])):
        score+=4
    elif (myTemp[0] == herTemp[0]):
        score+=1
    elif (myTemp[1] == herTemp[1]):
        score+=2
    else: score-=5
print('My   Activity:Location = ',end='')
for i in range(len(myPrintTemp)):
    if(i!=len(myPrintTemp)-1):
        print(myPrintTemp[i],end=', ')
    else:
        print(myPrintTemp[i])
print('Your Activity:Location = ',end='')
for i in range(len(herPrintTemp)):
    if(i!=len(herPrintTemp)-1):
        print(herPrintTemp[i],end=', ')
    else:
        print(herPrintTemp[i])
    
if(score >= 7):
    print('Yes! You\'re my love! : Score is '+str(score)+'.')
elif(0 < score < 7):
    print('Umm.. It\'s complicated relationship! : Score is '+str(score)+'.')
else:
    print('No! We\'re just friends. : Score is '+str(score)+'.')