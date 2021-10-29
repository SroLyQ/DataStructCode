#item : 5 - Exam #2 Stack Queue LinkedList 5b
class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p   
            self.tail =p  
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

def findMode(ll):
    listContent=[]
    listContentCount=[]
    p=ll.head
    while(p!=None):
        if p.data not in listContent:
            listContent.append(p.data)
            listContentCount.append(1)
        elif p.data in listContent:
            for i in range(len(listContent)):
                if listContent[i]==p.data:
                    listContentCount[i]+=1
                    break
        p=p.next
    m=-2000000000
    mode=[]
    for i in range(len(listContentCount)):
        if(listContentCount[i] > m):
            m=listContentCount[i]
    for i in range(len(listContentCount)):
        if(listContentCount[i]==m):
            mode.append(listContent[i])
    if len(mode) > 0 and len(mode)!=len(listContent):
        print('Mode =  '+str(mode).replace('[','').replace(']','').replace(',',''))
    else:
        print('Mode is not available.')

inputlist = [int(e) for e in input('Enter numbers : ').split()]
l = LinkedList()
for j in range(len(inputlist)):
    for i in range(len(inputlist)):
        if(i!=len(inputlist)-1):
            if inputlist[i]>inputlist[i+1]:
                temp=inputlist[i+1]
                inputlist[i+1]=inputlist[i]
                inputlist[i]=temp
            if inputlist[i+1]>=inputlist[i]:
                continue
for data in inputlist:
    l.append(data)
print("Output :")
print(l)
print('Amount of data =',len(l))
findMode(l)