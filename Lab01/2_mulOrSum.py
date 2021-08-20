print("*** multiplication or sum ***")
print("Enter num1 num2 : ",end='')
x,y=map(int,input().split(' '))
if(x*y>1000):
    print("The result is "+str(x+y))
elif(x*y<=1000):
    print("The result is "+str(x*y))