def range(*args):
    start = 0
    end = 0
    step = 1
    lis=[]
    if(len(args[0])==1):
        end=args[0][0]
    elif(len(args[0])==2):
        start,end = args[0]
    elif(len(args[0])==3):
        start,end,step = args[0]
    
    start = float(start)
    end = float(end)
    step = float(step)
    dec=[len(str(start).split('.')[1]),len(str(end).split('.')[1]),len(str(step).split('.')[1])]
    dec.sort();
    

    while(start < end):
        lis.append(round(start,dec[len(args[0])-1]))
        start+=step
    return lis
print('*** New Range ***')
num = input("Enter Input : ").split()
numlis = range(num)
print(tuple(numlis))
