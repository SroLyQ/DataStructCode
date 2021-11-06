class TreeNode(object):

    def __init__(self, x):

        self.val = x

        self.left = None

        self.right = None



def list_to_bst(list_nums):
    #code here
    if len(list_nums)==0:
        return None
    index = int(len(list_nums)/2)
    node = TreeNode(list_nums[index])
    temp=list_nums.copy()
    node.left = list_to_bst(temp[0:index])
    node.right = list_to_bst(temp[index+1:])
    return node



def preOrder(node): 

    if not node: 

        return      

    print(node.val)

    preOrder(node.left) 

    preOrder(node.right)   



def printBST(node,level = 0):

    if node != None:

        printBST(node.right, level + 1)

        print('     ' * level, node.val)

        printBST(node.left, level + 1)



list_nums = sorted([int(item) for item in input("Enter list : ").split()])

result = list_to_bst(list_nums)

print("\nList to a height balanced BST : ")

print(preOrder(result))

print("\nBST model : ")

printBST(result)