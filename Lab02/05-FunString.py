class funString():

    def __init__(self,string = ""):

        ### Enter Your Code Here ###
        self.string = string

    def __str__(self):
        ### Enter Your Code Here ###
        return self.string
    def size(self) :
        ### Enter Your Code Here ###
        return str(len(self.string))
    def changeSize(self):
        ### Enter Your Code Here ###
        temp=''
        for a in self.string:
            if(ord(a)<=90):
                tempChar=chr(ord(a)+32)
            else: tempChar=chr(ord(a)-32)
            temp+=tempChar
        return str(temp)
    def reverse(self):
        ### Enter Your Code Here ###
        temp=''
        for i in range(len(self.string)-1,-1,-1):
            temp+=self.string[i]
        return str(temp)
    def deleteSame(self):
       ### Enter Your Code Here ###
        usedChar=[]
        ansStr=''
        for a in self.string:
            if(a not in usedChar):
                usedChar.append(a)
                ansStr+=a
        return ansStr




str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)
if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())