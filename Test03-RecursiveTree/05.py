class Node:
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right= None
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            p=self.root
            while(p!=None):
                if(data < p.data):
                    if(p.left==None):
                        p.left = Node(data)
                        break
                    p=p.left
                else:
                    if(p.right == None):
                        p.right = Node(data)
                        break
                    p=p.right
    def preOrder(self,node):
        if node == None:
            return
        print(node,end = ' ')
        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self,node):
        if node == None:
            return
        self.inOrder(node.left)
        print(node,end = ' ')
        self.inOrder(node.right)

    def postOrder(self,node):
        if node == None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node,end = ' ')

    def bfs(self):
        p=self.root
        q=Queue()
        q.push(p)
        while(not q.isEmpty()):
            if q.front() == None:
                q.pop()
            else:
                print(q.front(),end = ' ')
                q.push(q.front().left)
                q.push(q.front().right)
                q.pop()
class Queue:
    def __init__(self):
        self.queue=[]
    def __str__(self):
        temp=''
        for i in range(len(self.queue)):
            if i != len(self.queue)-1:
                temp+=str(self.queue[i])
                temp+=' '
            else:
                temp+=str(self.queue[i])
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
    def reset(self):
        self.queue=[]

print(' *** Binary Search Tree ***')
inp=[int(e) for e in input('Enter Input : ').split()]
t=BST()
for i in inp:
    root=t.insert(i)
print('')
print(' --- Tree traversal ---')
print('Level order : ',end='')
t.bfs()
print('')
print('Preorder : ',end='')
t.preOrder(t.root)
print('')
print('Inorder : ',end='')
t.inOrder(t.root)
print('')
print('Postorder : ',end='')
t.postOrder(t.root)
print('')
