class SinglyLinkedList:     
    class Node :                    
        def __init__(self, data, next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
        def __str__(self):
            return self.data
        
    def __init__(self):                
            self.head = None
            self.tail = None
            self.size = 0
            
    def __str__(self):
        s=''
        p = self.head
        while p != None :
            if p!=self.tail:
                s += str(p.data) + ' <- '
            else:
                s += str(p.data)
            p = p.next
        return s
          
    def __len__(self) :               
        return self.size         
            
    def isEmpty(self) :               
        return self.size == 0         
        
    def indexOf(self,data) :          
        p = self.head
        for i in range(len(self)) :
            if p.data == data :
                return i
            p = p.next
        return -1
            
    def isIn(self,data) :          
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :             
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p
    
     
    def removeTail(self) :
        if self.size > 0 :
          q = self.nodeAt(len(self)-2)
          self.tail = q
          q.next = None
          self.size -= 1

    def deleteAfter(self,i) :           
        if self.size > 0 : 
          q = self.nodeAt(i)  
          q.next = q.next.next
          self.size -= 1
    
    def delete(self,i) :              
        if self.size > 0 :
          if i == 0 :
            self.head = self.head.next
            self.size -= 1
          elif i == len(self) - 1 :
            self.removeTail()
          else :
            self.deleteAfter(i-1)     
        
    def removeData(self,data) :          
        if self.isIn(data) :
            self.deleteAfter(self.indexOf(data)-1)
          
    def addHead(self,data) :
        if self.isEmpty() :
          p = self.Node(data)
          self.head = p
          self.size += 1
        else :
          p = self.Node(data,self.head)
          self.head = p
          self.size += 1
print(' *** Locomotive ***')
inp=input('Enter Input : ').split(' ')
ll=SinglyLinkedList()
for a in inp:
    ll.push(a)
print('Before : ' + str(ll))
while ll.head.data != '0':
    temp=ll.head
    ll.push(temp)
    ll.delete(0)
print('After : ' + str(ll))
    
