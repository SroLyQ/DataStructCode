class Queue:
    def __init__(self):
        self.queue=[]
    def __str__(self):
        temp=''
        for i in range(len(self.queue)):
            if i != len(self.queue)-1:
                temp+=self.queue[i]
                temp+=', '
            else:
                temp+=self.queue[i]
        return str(temp)
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

op=input("Enter Input : ").split(',')
q=Queue()
poped=[]
for i in range(len(op)):
    if(op[i][0]=='E'):
        q.push(op[i][2])
        if(not q.isEmpty()):
            print(q)
        else:
            print('Empty')
    elif(op[i][0]=='D'):
        if(not q.isEmpty()):
            temp=q.pop()
            poped.append(temp)
            print(temp,end=' <- ')
            if(not q.isEmpty()):
                print(q)
            else:
                print('Empty')
        else:
            print('Empty')
    if(i == len(op)-1):
        if(len(poped)!=0):
            for i in range(len(poped)):
                if i != len(poped)-1:
                    print(poped[i],end=', ')
                else:
                    print(poped[i],end=' : ')
        else:
            print('Empty',end=' : ')
        if(not q.isEmpty()):
            print(q)
        else:
            print('Empty')

        