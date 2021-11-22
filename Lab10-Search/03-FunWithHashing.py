class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,maxSize,maxCol,nowCol=0):
        self.table=[]
        for i in range(maxSize):
            self.table.append(None)
        self.maxSize=maxSize
        self.maxCol = maxCol

    def insert(self,key,value):
        index=0
        if(not self.isFull()):
            for cha in list(key):
                index+=ord(cha)%self.maxSize
            index%=self.maxSize
            if(self.table[index]==None):
                self.table[index]=Data(key,value)
            elif self.table[index]!=None:
                r=0
                newIndex = index
                print('collision number {0} at {1}'.format(r+1,newIndex))
                while(self.table[newIndex]!=None):
                    r+=1 
                    newIndex = (index + (r**2)) % self.maxSize
                    if(self.table[newIndex]==None):
                        self.table[newIndex]=Data(key,value)
                        break
                    #print(self.maxCol)
                    #print(self.nowCol)
                    if(self.maxCol <= r):
                        print('Max of collisionChain')
                        break  
                    print('collision number {0} at {1}'.format(r+1,newIndex))
            return True
        else:
            return False
    def isFull(self):
        for i in self.table:
            if i == None:
                return False
        return True
    
    def print(self):
        for i in range(len(self.table)):
            print('#{0}      {1}'.format(i+1,self.table[i]))

print(' ***** Fun with hashing *****')
inp1,inp2=input('Enter Input : ').split('/')
sizeTable,maxCol=inp1.split()
inp2=[e for e in inp2.split(',')]
hashTable = hash(int(sizeTable),int(maxCol))
for i in inp2:
    if(hashTable.insert(i.split()[0],i.split()[1])):
        hashTable.print()
        print('---------------------------')
    else:
        print('This table is full !!!!!!')
        break
