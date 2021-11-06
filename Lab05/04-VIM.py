class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    def __str__(self):
        return self.data
class DoublyLinkedList:     
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def __len__(self):
        return self.size
    def __str__(self):
        s=''
        p = self.head
        while p != None :
            if p!=self.tail:
                s += str(p.data) + ' '
            else:
                s += str(p.data)
            p = p.next
        return s
    def isEmpty(self):
        if self.size == 0 :
            return True
        else:
            return False
    def append(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next=temp
            temp.prev=self.tail
            self.tail=self.tail.next
        self.size+=1
    def insert(self, index, data):
        i=0
        temp = Node(data)
        p=self.head
        if index==0:
            if(self.isEmpty()):
                self.head=temp
                self.tail=temp
            else:
                self.head.prev=temp
                temp.next=self.head
                self.head=temp
        elif index==len(self):
            self.size-=1
            self.append(data)
        else:
            while i != index:
                if i==index-1:
                    temp.prev=p
                    temp.next=p.next
                    p.next.prev=temp
                    p.next=temp
                else:
                    p=p.next
                i+=1
        self.size+=1
    def isin(self,data):
        i=0
        p=self.head
        if self.head != self.tail:
            while p!=None:
                if(p.data == data):
                    return i
                else:
                    p=p.next
                    i+=1
        elif self.head == self.tail:
            return 0
        return -1
    def deleteAt(self,index):
        i=0
        p=self.head
        
        while i!=index:
            i+=1
            if p.next != None:
                p=p.next
            else:
                return None
        if(p!=self.head and p!=self.tail ):
            p.prev.next=p.next
            p.next.prev=p.prev
        elif p==self.head :
            p.next.prev=None
            self.head=p.next
            p.next=None
        elif p==self.tail :
            p.prev.next=None
            self.tail=p.prev
            p.prev=None
        self.size-=1
        return p

    def remove(self,data):
        p=self.head
        i=0
        while p != None:
            if p.data == data:
                if p != self.head and p != self.tail:
                    p.prev.next=p.next
                    p.next.prev=p.prev
                    p.prev=None
                    p.next=None
                elif p==self.head and self.head != self.tail:
                    p.next.prev=None
                    self.head=p.next
                    p.next=None
                elif p==self.tail and self.head != self.tail:
                    p.prev.next=None
                    self.tail=p.prev
                    p.prev=None
                else :
                    self.head=None
                    self.tail=None
                self.size-=1
                return [p,i]
            p=p.next
            i+=1
        return [None]
inp = input('Enter Input : ').split(',')
ll = DoublyLinkedList();
ll.append('|')
for op in inp:
    op=op.split(' ')
    index = ll.isin('|')
    if op[0]=='I':
        ll.insert(index,op[1])
    elif op[0]=='L':
        if index != 0 :
            ll.remove('|')
            ll.insert(index-1,'|')
    elif op[0]=='R':
        if index != len(ll)-1:
            ll.remove('|')
            ll.insert(index+1,'|')
    elif op[0]=='B':
        ll.deleteAt(index-1)
    elif op[0]=='D':
        ll.deleteAt(index+1)
print(ll)