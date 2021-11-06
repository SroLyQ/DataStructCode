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
def multiply(node,k):
    if node == None:
        return
    if node.data > k:
        node.data*=3
    multiply(node.left,k)
    multiply(node.right,k)
T1= BST()
inp = input('Enter Input : ')
dataList = inp.split('/')[0].split(' ')
for i in dataList:
    T1.insert(int(i))
k=int(inp.split('/')[1])
T1.printTree(T1.root)
print('--------------------------------------------------')
multiply(T1.root,k)
T1.printTree(T1.root)
