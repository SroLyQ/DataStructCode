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

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

def closestValue(root,vaule):
    if root == None:
        return
    closestValue(root.left,vaule)
    newLis.append(root.data)
    closestValue(root.right,vaule)

    for i in range(len(newLis)):
        if vaule <= newLis[0]:
            return newLis[0]
        elif i+1 < len(newLis) and newLis[i] < vaule and newLis[i+1] >= vaule:
            return newLis[i+1]
        elif i+1 == len(newLis):
            return newLis[len(newLis)-1]
    

inp,val=input('Enter Input : ').split('/')
inpLis = [int(e) for e in inp.split()]
newLis=[]
T = BST()
for data in inpLis:
    T.insert(data)
    T.printTree(T.root)
    print('--------------------------------------------------')
ans=closestValue(T.root,int(val))
print('Closest value of {0} : '.format(str(val))+str(ans))
