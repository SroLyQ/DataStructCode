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
T1= BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T1.insert(i)
print('Height of this tree is : '+str(T1.level))