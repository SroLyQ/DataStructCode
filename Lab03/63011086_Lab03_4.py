class Stack:

    def __init__(self, ls=None):
        self.ls=[]
    def push(self,i):
        self.ls.append(i)
    def pop(self):
        a=self.ls.pop()
        return a
    def isEmpty(self):
        if(len(self.ls)==0):
            return True
        else:
            return False
    def size(self):
        return len(self.ls)
def stackCalculator(st):
    s = Stack()
    ### Enter Your Code Here ###
    for op in st:
        if(op=='+'):
            a=s.pop()
            b=s.pop()
            s.push(a+b)
        elif(op=='-'):
            a=s.pop()
            b=s.pop()
            s.push(a-b)
        elif(op=='*'):
            a=s.pop()
            b=s.pop()
            s.push(a*b)
        elif(op=='/'):
            a=s.pop()
            b=s.pop()
            s.push(a/b)
        elif(op=='DUP'):
            a=s.pop()
            s.push(a)
            s.push(a)
        elif(op=='POP'):
            s.pop()
        elif(op=='PUSH'):
            s.push()
        elif(op.isalpha()):
            return 'Invalid instruction: '+op
        else:
            s.push(int(op));
    if(s.isEmpty() == False):
        return int(s.pop())
    else:
        return 0
class StackCalc:
    def __init__(self):
        self.ans=0
    def run(self,arg):
        inp=arg.split();
        self.ans=stackCalculator(inp)
        if(self.ans==''):
            self.ans=0
    def getValue(self):
        return self.ans

print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())