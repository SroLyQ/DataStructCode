class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
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
                s += str(p.data) + '->'
            else:
                s += str(p.data)
            p = p.next
        return s
    def str_reverse(self):
        s=''
        p=self.tail
        while p != None :
            if p!=self.head:
                s += str(p.data) + '->'
            else:
                s += str(p.data)
            p = p.prev
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
inp = input('Enter Input : ')
inpNew=inp.replace(', ',',').split(',')
ll=DoublyLinkedList()
for op in inpNew:
    op=op.split(' ')
    if op[0]=='A':
        ll.append(op[1])
        print('linked list : ' + str(ll))
        print('reverse : ' + ll.str_reverse())
    elif op[0]=='Ab':
        ll.insert(0,op[1])
        print('linked list : ' + str(ll))
        print('reverse : ' + ll.str_reverse())
            
    elif op[0]=='I':
        temp=op[1].split(':')
        if int(temp[0]) < 0 or int(temp[0]) > len(ll):
            print('Data cannot be added')
            print('linked list : ' + str(ll))
            print('reverse : ' + ll.str_reverse())
        else:
            ll.insert(int(temp[0]),temp[1])
            print('index = '+ temp[0] + ' and data = ' + temp[1])
            print('linked list : ' + str(ll))
            print('reverse : ' + ll.str_reverse())
    elif op[0]=='R':
        t = ll.remove(op[1])
        if t[0]==None:
            print('Not Found!')
            print('linked list : ' + str(ll))
            print('reverse : ' + ll.str_reverse())
        else:
            print('removed : ' + str(t[0].data) + ' from index : '+ str(t[1]))
            print('linked list : ' + str(ll))
            print('reverse : ' + ll.str_reverse())