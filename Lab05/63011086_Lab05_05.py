class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
def createLL(LL):
    # Code Here
    head = Node(LL[0])
    temp = head
    for i in range(1,len(LL)):
        newTemp = Node(LL[i])
        temp.next=newTemp
        temp=newTemp
    return head
def printLL(head):
    # Code Here
    temp=head
    string=''
    while temp!=None:
        string+=str(temp)
        string+=' '
        temp=temp.next
    return string
def SIZE(head):
    # Code Here
    cnt=1
    temp=head
    while temp.next!=None:
        cnt+=1
        temp=temp.next
    return cnt

def scarmble(head, b, r, size):
    # Code Here
    #---------------BottomUP------------------------
    opSize = size
    opSize *= b/100
    opSize=int(opSize)
    tail=head
    i=0
    while tail.next!=None:
        tail=tail.next
    tail.next = head
    temp = head
    while i < opSize:
        if i==opSize-1:
            head = temp.next
            temp.next = None
        temp=temp.next
        i+=1
    print('BottomUp {0:.3f} % : '.format(b)+'{0}'.format(printLL(head)))
    #----------------Riffle--------------------------
    opSize = size
    opSize *=r/100
    opSize = int(opSize)
    newEnd = False
    oldHead = head
    newHead = head
    i=0
    temp=oldHead
    while i < opSize:
        if i==opSize-1:
            newHead=temp.next
            temp.next=None
        temp=temp.next
        i+=1
    s=0
    if SIZE(oldHead)<SIZE(newHead):
        s=SIZE(oldHead)
        newEnd=True
    else :s=SIZE(newHead)
    i=0
    temp=oldHead
    newTemp=newHead
    while i < s:
        tempNext=temp.next
        newTempNext=newTemp.next
        if temp.next!=None and newTemp.next!=None:
            tempNext=temp.next
            temp.next=newTemp
            newTempNext=newTemp.next
            newTemp.next=tempNext
            newTemp=newTempNext
        elif temp.next !=None and newTemp.next==None:
            tempNext=temp.next
            temp.next=newTemp
            newTemp.next=tempNext
        elif temp.next == None and newTemp.next!=None:
            temp.next=newTemp
        elif temp.next == None and newTemp.next==None:
            temp.next = newTemp
        temp=tempNext
        newTemp=newTempNext
        i+=1
    head = oldHead
    print('Riffle {0:.3f} % : '.format(r)+'{0}'.format(printLL(head)))
    #----------------DeRiffle--------------------------
    opSize = s
    i=0
    if newEnd:
        temp=head
        while i < (2*opSize)-1:
            if i == (2*opSize)-2:
                oldTail=temp
            temp=temp.next
            i+=1
        i=0
        oldTailnext=oldTail.next
        temp=head
        while i < opSize-1:
            oldTail.next=temp.next
            oldTail=temp.next
            temp.next=temp.next.next
            oldTail.next=None
            temp=temp.next
            i+=1
        oldTail.next=oldTailnext
    else :
        temp=head
        while temp.next != None:
            temp=temp.next
        tail=temp
        temp=head
        while i < opSize:
            tail.next = temp.next
            tail=tail.next
            temp.next = temp.next.next
            tail.next=None
            temp = temp.next
            i+=1
    print('Deriffle {0:.3f} % : '.format(r)+'{0}'.format(printLL(head)))
    #----------------Debottomup--------------------------
    opSize = size
    opSize *= b/100
    opSize=size-int(opSize)
    tail=head
    i=0
    while tail.next!=None:
        tail=tail.next
    tail.next = head
    temp = head
    while i < opSize:
        if i==opSize-1:
            head = temp.next
            temp.next = None
        temp=temp.next
        i+=1
    print('Debottomup {0:.3f} % : '.format(b)+'{0}'.format(printLL(head)))
    

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)