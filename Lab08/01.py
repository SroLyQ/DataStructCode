class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data[0])

class BST:
    def __init__(self):
        self.root = None
    def setRoot(self,node):
        self.root = node
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        elif self.root != None:
            p=self.root
            while(p!=None):
                if data >= p.data:
                    if p.right == None:
                        p.right = Node(data)
                        break
                    p=p.right

                elif data < p.data:
                    if p.left == None:
                        p.left = Node(data)
                        break
                    p=p.left
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

class Stack:
    def __init__(self):
        self.items = []
    def __str__(self):
        s=''
        for i in self.items:
            s+=str(i)
            s+=', '
        return s
    def reverse(self):
        self.items.reverse()
    def push(self,i):
        self.items.append(i)
    def top(self):
        if self.size() != 0:
            return self.items[len(self.items)-1]
    def pop(self):
        if not self.isEmpty():
            poped=self.items.pop(len(self.items)-1)
            return poped
    def isEmpty(self):
        if(len(self.items)==0):
            return True
        else: 
            return False
    def size(self):
        return len(self.items)

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

inp = input('Enter Input : ')
count = {}
for i in inp:
    if i not in count:
        count.update({i:1})
    else:
        count[i]+=1
sort_count = dict(sorted(count.items(), key=lambda x: x[::-1]))
st=Stack()
for i in sort_count.items():
    st.push(Node(i))
st.reverse()
print(st)
st2=Stack()
while(not st.isEmpty()):
    if(not st.isEmpty()):
        pop1 = st.pop()
    if(not st.isEmpty()):
        pop2 = st.pop()
    #print(str(pop1)+' and '+str(pop2))
    T=Node(('*',pop1.data[1]+pop2.data[1]))
    T.left = pop1
    T.right =  pop2
    if not st.isEmpty():
        while st.top().data[1]<T.data[1]:
            st2.push(st.pop())
            if st.isEmpty():
                break
        st.push(T)
        while not st2.isEmpty():
            st.push(st2.pop())
            if st2.isEmpty():
                break
    root=T
bst = BST()
bst.setRoot(root)
bst.printTree(bst.root)
