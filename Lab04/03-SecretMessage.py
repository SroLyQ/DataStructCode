class Queue:
    def __init__(self):
        self.queue=[]
    def __str__(self):
        return str(self.queue)
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
def encodemsg(data,key):
    tempQ = Queue()
    tempK = Queue()
    for i in range(key.size()):
        temp = key.pop()
        tempK.push(temp)
        key.push(temp)
    while(not data.isEmpty()):
        char = data.pop()
        tempKey = key.pop()
        if ord('A') <= ord(char) <= ord('Z'):
            tempInt=((ord(char)+tempKey)-ord('A'))%26+ord('A')
            tempQ.push(chr(tempInt))
        elif ord('a') <= ord(char) <= ord('z'):
            tempInt=((ord(char)+tempKey)-ord('a'))%26+ord('a')
            tempQ.push(chr(tempInt))
        key.push(tempKey)
    while(not tempQ.isEmpty()):
        data.push(tempQ.pop())
    while(not key.isEmpty()):
        key.pop()
    while(not tempK.isEmpty()):
        key.push(tempK.pop())
    return data
def decodemsg(data,key):
    tempQ = Queue()
    tempK = Queue()
    for i in range(key.size()):
        temp = key.pop()
        tempK.push(temp)
        key.push(temp)
    while(not data.isEmpty()):
        char = data.pop()
        tempKey = key.pop()
        if ord('A') <= ord(char) <= ord('Z'):
            tempInt=((ord(char)-tempKey)-ord('A'))%26+ord('A')
            tempQ.push(chr(tempInt))
        elif ord('a') <= ord(char) <= ord('z'):
            tempInt=((ord(char)-tempKey)-ord('a'))%26+ord('a')
            tempQ.push(chr(tempInt))
        key.push(tempKey)
    while(not tempQ.isEmpty()):
        data.push(tempQ.pop())
    while(not key.isEmpty()):
        key.pop()
    while(not tempK.isEmpty()):
        key.push(tempK.pop())
    return data
inp = input("Enter String and Code : ").split(',')
number=list(inp[1])
string=list(inp[0])

q1 = Queue()

q2 = Queue()
for a in number:
    q2.push(int(a))
for a in string:
    if a != ' ':
        q1.push(a)

print('Encode message is :  ' + str(encodemsg(q1, q2)))
print('Decode message is :  ' + str(decodemsg(q1, q2)))
"""
print('Decode message is : ' + str(decodemsg(q1, q2)))
encodemsg(q1, q2)
decodemsg(q1, q2)
"""