#item : 1 - Exam #2 Stack Queue LinkedList 1a
class Stack:
    def __init__(self):
        self.stack = []
    def __str__(self):
        return 'Data in Stack is : '+str(self.stack).replace('[','').replace(']','').replace(',','')
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if(len(self.stack) > 0):
            return self.stack.pop()
    def isEmpty(self):
        if(len(self.stack)== 0):
            return True
        return False
    def size(self):
        return len(self.stack)
    def peek(self):
        if(len(self.stack) > 0):
            return self.stack[len(self.stack)-1]
    def bottom(self):
        if(len(self.stack) > 0):
            return self.stack[0]
choice = int(input('Enter choice : '))
if choice == 1:
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())
elif choice == 2:
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :",s1.isEmpty())
elif choice == 3:
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :",s1.size())