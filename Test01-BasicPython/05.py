class MyInt:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        ans=self.value+other.value
        ans+=ans/2
        return ans
    def toRoman(self):
        temp=self.value
        roman=''
        while temp != 0:
            if(temp>=1000):
                temp-=1000
                roman+='M'
            elif(temp >= 900):
                temp-=900
                roman+='CM'
            elif temp >= 500:
                temp-=500
                roman+='D'
            elif temp >=400:
                temp-=400
                roman+='CD'
            elif temp >=100:
                temp-=100
                roman+='C'
            elif temp >= 90:
                temp-=90
                roman+='XC'
            elif temp >=50:
                temp -= 50
                roman += 'L'
            elif temp >=40:
                temp -= 40
                roman += 'XL'
            elif temp >=10:
                temp -= 10
                roman += 'X'
            elif temp >=9:
                temp -= 9
                roman += 'IX'
            elif temp >=5:
                temp -= 5
                roman += 'V'
            elif temp >=4:
                temp -= 4
                roman += 'IV'
            elif temp >=1:
                temp -= 1
                roman += 'I'
        return roman
print(' *** class MyInt ***')
a,b =map(int,input('Enter 2 number : ').split(' '))
i=a
j=b
a = MyInt(a)

b = MyInt(b)

print('{0} convert to Roman : {1}'.format(i,a.toRoman()))

print('{0} convert to Roman : {1}'.format(j,b.toRoman()))

print('{0} + {1} = {2}'.format(i,j,int(a+b)))

