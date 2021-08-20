print('*** Reading E-Book ***')
x,y=input('Text , Highlight : ').split(',')
for a in x:
    if(a==y):
        print('['+a+']',end='')
    else:
        print(a,end='')