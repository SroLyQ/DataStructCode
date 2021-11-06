class Stack():

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
def postFixeval(st):
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
            s.push(b-a)
        elif(op=='*'):
            a=s.pop()
            b=s.pop()
            s.push(a*b)
        elif(op=='/'):
            a=s.pop()
            b=s.pop()
            s.push(b/a)
        elif(op=='^'):
            a=s.pop()
            b=s.pop()
            s.push(b**a)
        else:
            s.push(int(op));
    return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))