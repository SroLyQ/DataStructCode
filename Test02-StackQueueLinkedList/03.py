#item : 3 - Exam #2 Stack Queue LinkedList 3b
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
    def removeDup(self):
        dup=[]
        p=self.head
        if p != None:
            dup.append(p.data)
        while(p!=None):
            if p.next != None and p.next.data not in dup :
                dup.append(p.next.data)
                p=p.next
            elif p.next != None and p.next.data in dup:
               q=p.next.next
               p.next = q
            elif p.next == None:
                break
inputlist = [int(e) for e in input('Enter numbers : ').split()]

l = LinkedList()
for i in inputlist:
    l.append(i)
print("Linkedlist Before removeDuplicate")
print(l)
print("Linkedlist After removeDuplicate")
l.removeDup()
print(l)             