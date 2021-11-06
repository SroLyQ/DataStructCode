class Stack:
    def __init__(self):
        self.items = []
    def push(self,i):
        self.items.append(i)
    def pop(self):
        return self.items.pop(len(self.items)-1)
    def isEmpty(self):
        if(len(self.items)==0):
            return True
        else: 
            return False
    def size(self):
        return len(self.items)
    def top(self):
        if(len(self.items)!=0):
            return self.items[len(self.items)-1]
print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)

### Enter Your Code Here ###
soi1 = Stack()
soi2 = Stack()
if(len(s)==1 and s[0]=='0'):
    s=[]
else:
    s=s.split(',')
    for a in s:
        a=int(a)
        soi1.push(a)
if(o == 'arrive'):
    if(m<=soi1.size()):
        print('car '+str(n)+' cannot arrive : Soi Full')
    elif(n in soi1.items):
        print('car '+str(n)+' already in soi')
    else:
        soi1.push(n)
        print('car '+str(n)+' arrive! : Add Car '+str(n))
elif(o == 'depart'):
    if(soi1.size() == 0):
        print('car '+str(n)+' cannot depart : Soi Empty')
    elif(n not in soi1.items):
        print('car '+str(n)+' cannot depart : Dont Have Car '+str(n))
    else:
        temp=-1
        while(temp != n and not soi1.isEmpty()):
            temp=soi1.pop()
            if(temp==n):
                print('car '+str(n)+' depart ! : Car '+str(n)+' was remove')
                while(not soi2.isEmpty()):
                    soi1.push(soi2.pop())
            else:
                soi2.push(temp)
print(soi1.items)
