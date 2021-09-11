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
ip=list(input('Enter people : '))
minute=0
mainQ=Queue()
cashier1Q=Queue()
cashier2Q=Queue()
for person in ip:
    mainQ.push(person);
while(not mainQ.isEmpty()):
    minute+=1
    print(minute,end=' ')
    if(minute%3==1):
        if(not cashier1Q.isEmpty()):
            cashier1Q.pop()
    if(minute%2==0):
        if(not cashier2Q.isEmpty()):
            cashier2Q.pop()
    if cashier1Q.size() != 5:
        cashier1Q.push(mainQ.pop())
    else:
        cashier2Q.push(mainQ.pop())
    print(mainQ,end=' ')
    print(cashier1Q,end=' ')
    print(cashier2Q)



