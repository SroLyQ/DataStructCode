

class Stack:
    def __init__(self):
        self.items = []
    def push(self,i):
        self.items.append(i)
    def pop(self):
        self.items.pop(len(self.items)-1)
    def isEmpty(self):
        if(len(self.items)==0):
            return True
        else: 
            return False
    def size(self):
        return len(self.items)
    def top(self):
        if(len(self.items)!=0):
            return self.items[len(self.items)-1]

lis = input("Enter expresion : ")
st = Stack()
ch = False
cnt = 0
for a in lis :
    if(a == '(' or a == '[' or a == '{'):
        st.push(a)
    elif(a==')'):
        if(st.top()=='('):
            st.pop()
        elif(st.isEmpty()):
            cnt+=1
        else: 
            ch=True
            break;
    elif(a==']'):
        if(st.top()=='['):
            st.pop()
        elif(st.isEmpty()):
            cnt+=1
        else: 
            ch=True
            break;
    elif(a=='}'):
        if(st.top()=='{'):
            st.pop()
        elif(st.isEmpty()):
            cnt+=1
        else: 
            ch=True
            break;
if(ch):
    print(lis+' Unmatch open-close')
else:
    if(st.top()=='(' or st.top()=='[' or st.top()=='{'):
        print(lis+' open paren excess   '+str(st.size())+' : ',end='')
        for a in st.items:
            print(a,end='')
    elif(cnt!=0):
        print(lis +' close paren excess')
    else:
        print(lis+' MATCH')

#ไปหัดเขียนคำว่า expression มาใหม่นะ