class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.level = 0

    def insert(self, data):
        level = 0
        if self.root == None:
            self.root = Node(data)
        elif self.root != None:
            p=self.root
            while(p!=None):
                level+=1
                if data >= p.data:
                    if p.right == None:
                        self.level = max(level,self.level)
                        p.right = Node(data)
                        break
                    p=p.right

                elif data < p.data:
                    if p.left == None:
                        self.level = max(level,self.level)
                        p.left = Node(data)
                        break
                    p=p.left
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

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

def preOrder(node):
    if(node == None):
        return
    q.push(node.data)
    preOrder(node.left)
    preOrder(node.right)

def inOrder(node):
    if(node == None):
        return
    inOrder(node.left)
    q.push(node.data)
    inOrder(node.right)

def postOrder(node):
    if(node == None):
        return
    postOrder(node.left)
    postOrder(node.right)
    q.push(node.data)

def BFS(root):
    bfs=Queue()
    bfs.push(root)
    while(not bfs.isEmpty()):
        nextLeft=bfs.front().left
        nextRight=bfs.front().right
        if(nextLeft != None):
            bfs.push(nextLeft)
        if(nextRight != None):
            bfs.push(nextRight)
        q.push(bfs.pop())

q=Queue()
t=BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for data in inp:
    t.insert(data)
preOrder(t.root)
print('Preorder : '+ str(q))
q=Queue()
inOrder(t.root)
print('Inorder : '+ str(q))
q=Queue()
postOrder(t.root)
print('Postorder : '+ str(q))
q=Queue()
BFS(t.root)
print('Breadth : '+ str(q))