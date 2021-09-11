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
class Stack():

    def __init__(self, ls=None):
        self.ls=[]
    def __str__(self):
        return str(self.ls)
    def push(self,i):
        self.ls.append(i)
    def pop(self):
        a=self.ls.pop()
        return a
    def isEmpty(self):
        if(len(self.ls)==0):
            return True
        else:
            return False
    def size(self):
        return len(self.ls)
    def top(self):
        if len(self.ls)==0:
            return False
        return self.ls[len(self.ls)-1]
inp=input('Enter Input (Normal, Mirror) : ').split(' ')
nL,mL = inp
list(nL)
list(mL)
stCh=Stack()
stM=Stack()
stN=Stack()
mQ = Queue()
nQ = Queue()
for i in nL:
    nQ.push(i)
for i in mL:
    stM.push(i)
while not stM.isEmpty():
    mQ.push(stM.pop())
leftMList=[]
leftNList=[]
inRow = False
numExM = 0
numExN = 0
numInter=0
while(not mQ.isEmpty()):
    temp=mQ.pop()
    if stCh.isEmpty():
        stCh.push(temp)
    else:
        if stCh.top() == temp and inRow:
            stCh.pop()
            stM.push(stCh.pop())
            numExM+=1
            temp1=''
            if not stCh.isEmpty():
                temp1=stCh.pop()
                if temp1==stCh.top():
                        inRow=True
                        stCh.push(temp1)
                else :
                        inRow=False
                        stCh.push(temp1)
            else :
                inRow=False
        elif stCh.top() == temp and not inRow:
            stCh.push(temp)
            inRow=True
        else:
            stCh.push(temp)
            inRow=False
items=Queue()
tempSt=Stack()
while(not stM.isEmpty()):
    tempSt.push(stM.pop())
while(not tempSt.isEmpty()):
    items.push(tempSt.pop())
while(not stCh.isEmpty()):
    tempSt.push(stCh.pop())
while(not tempSt.isEmpty()):
    leftMList.append(tempSt.pop())
'''
print(leftMList)
print(numExM)
print(items)
'''
inRow = False
while not nQ.isEmpty():
    temp=nQ.pop()
    if stCh.isEmpty():
        stCh.push(temp)
    else:
        if stCh.top() == temp and inRow:
            if(items.isEmpty() and temp!=items.front()):
                stCh.pop()
                stCh.pop()
                temp1=''
                if not stCh.isEmpty():
                    temp1=stCh.pop()
                    if temp1==stCh.top():
                        inRow=True
                        stCh.push(temp1)
                    else :
                        inRow=False
                        stCh.push(temp1)
                else :
                    inRow=False
                numExN+=1
            elif not items.isEmpty() and temp!=items.front():
                stCh.push(items.pop())
                stCh.push(temp)
                inRow=False
            elif not items.isEmpty() and temp == items.front():
                stCh.pop()
                stCh.pop()
                numInter+=1
                stCh.push(items.pop())
                temp1=''
                if not stCh.isEmpty():
                    temp1=stCh.pop()
                    if temp1==stCh.top():
                        inRow=True
                        stCh.push(temp1)
                    else :
                        inRow=False
                        stCh.push(temp1)
                else :
                    inRow=False
        elif stCh.top() == temp and not inRow:
            stCh.push(temp)
            inRow=True
        else:
            stCh.push(temp)
            inRow=False
while(not stCh.isEmpty()):
    leftNList.append(stCh.pop())
    '''
print(leftNList)
print(numExN)
    '''
print('NORMAL : ')
print(len(leftNList))
if(len(leftNList)!=0):
    for i in leftNList:
        print(i,end='')
    print('')
else:
    print('Empty')
print(str(numExN)+' Explosive(s) ! ! ! (NORMAL)')
if numInter!=0:
    print('Failed Interrupted '+str(numInter)+' Bomb(s)')
print('------------MIRROR------------')
print(': RORRIM')
print(len(leftMList))
if(len(leftMList)!=0):
    for i in range(len(leftMList)-1,-1,-1):
        print(leftMList[i],end='')
    print('')
else:
    print('ytpmE')
print('(RORRIM) ! ! ! (s)evisolpxE '+str(numExM))