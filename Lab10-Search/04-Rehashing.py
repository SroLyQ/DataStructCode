class hash:
    def __init__(self,maxSize,maxCol,Threshold):
        self.table=[]
        for i in range(maxSize):
            self.table.append(None)
        self.maxSize=maxSize
        self.maxCol = maxCol
        self.Threshold=Threshold
    def insert(self,value):
        index=0
        if(not self.isFull()):
            index=value%self.maxSize
            if(self.table[index]==None):
                self.table[index]=value
            elif self.table[index]!=None:
                r=0
                newIndex = index
                print('collision number {0} at {1}'.format(r+1,newIndex))
                while(self.table[newIndex]!=None):
                    r+=1 
                    newIndex = (index + (r**2)) % self.maxSize
                    if(self.maxCol <= r):
                        print('****** Max collision - Rehash !!! ******')
                        return False
                    if(self.table[newIndex]==None):
                        self.table[newIndex]=value
                        break
                    #print(self.maxCol)
                    #print(self.nowCol)
                    print('collision number {0} at {1}'.format(r+1,newIndex))
            return True
        else:
            print('****** Data over threshold - Rehash !!! ******')
            return False
    def isFull(self):
        k=int(self.maxSize*self.Threshold/100)
        leng=0
        for i in self.table:
            if i != None:
                leng+=1
        if leng>=k:
            return True
        return False
    
    def print(self):
        for i in range(len(self.table)):
            print('#{0}'.format(i+1),end='')
            print(' '*(7-len(str(i+1))),end='')
            print('{0}'.format(self.table[i]))

def findClosest(value):
    while True:
        value+=1
        for i in range(2,value):
            if value%i==0:
                break
            if i==value-1:
                return value
    
print(' ***** Rehashing *****')
inp1,inp2=input('Enter Input : ').split('/')
sizeTable,maxCol,Threshold=map(int,inp1.split())
inp2=[int(e) for e in inp2.split()]
print('Initial Table :')
global hashTable
hashTable = hash(sizeTable,maxCol,Threshold)
hashTable.print()
print('----------------------------------------')
hashTable.isFull()
lastAdd=-1
notAlldata=True
while(notAlldata):
    for i in range(len(inp2)):
        if(i >= lastAdd+1):
            print('Add : ' + str(inp2[i]))
        if(not hashTable.insert(inp2[i])):
            hashTable=hash(findClosest(hashTable.maxSize*2),maxCol,Threshold)
            lastAdd = i
            break
        else:
            if(i >= lastAdd):
                hashTable.print()
                print('----------------------------------------')
        if i == len(inp2)-1:
            notAlldata=False
