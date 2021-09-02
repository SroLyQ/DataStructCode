class translator:

    def deciToRoman(self, num):
        numTemp=num
        s=''
        while(numTemp!=0):
            if(numTemp>=1000):
                s+='M'
                numTemp-=1000
            elif(numTemp >= 900):
                s+="CM"
                numTemp-=900
            elif(numTemp >= 500):
                s+='D'
                numTemp-=500
            elif(numTemp >= 400):
                s+='CD'
                numTemp-=400
            elif(numTemp >= 100):
                s+='C'
                numTemp-=100
            elif(numTemp >= 90):
                s+='XC'
                numTemp-=90
            elif(numTemp >= 50):
                s+='L'
                numTemp-=50
            elif(numTemp >= 40):
                s+='XL'
                numTemp-=40
            elif(numTemp >= 10):
                s+='X'
                numTemp-=10
            elif(numTemp >= 9):
                s+='IX'
                numTemp-=9
            elif(numTemp >= 5):
                s+='V'
                numTemp-=5
            elif(numTemp >= 4):
                s+='IV'
                numTemp-=4
            elif(numTemp >= 1):
                s+='I'
                numTemp-=1
        return s
        ### Enter Your Code Here ###

    def romanToDeci(self, s):
        sTemp = str(s)
        num=0
        skip=False
        for i in range(len(sTemp)) :
            if(skip):
                skip=False
                continue
            if(sTemp[i]=='C' and i+1 < len(sTemp) and sTemp[i+1]=='M' ):
                num+=900
                skip=True
            elif(sTemp[i]=='M'):
                num+=1000
            elif(sTemp[i]=='C'and i+1 < len(sTemp) and sTemp[i+1]=='D' ):
                num+=400
                skip=True
            elif(sTemp[i]=='D'):
                num+=500
            elif(sTemp[i]=='C'):
                num+=100
            elif(sTemp[i]=='X'and i+1 < len(sTemp) and sTemp[i+1]=='C' ):
                num+=90
                skip=True
            elif(sTemp[i]=='L'):
                num+=50
            elif(sTemp[i]=='X' and i+1 < len(sTemp)and sTemp[i+1]=='L' ):
                num+=40
                skip=True
            elif(sTemp[i]=='X'):
                num+=10
            elif(sTemp[i]=='I' and i+1 < len(sTemp)and sTemp[i+1]=='X' ):
                num+=9
                skip=True
            elif(sTemp[i]=='V'):
                num+=5
            elif(sTemp[i]=='I' and i+1 < len(sTemp)and sTemp[i+1]=='V' ):
                num+=4
                skip=True
            elif(sTemp[i] == 'I'):
                num+=1
        return num
        ### Enter Your Code Here ###

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))