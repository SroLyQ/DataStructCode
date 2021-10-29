
print(' *** Divisible number ***')
inp=input('Enter a positive number : ')
inp = int(inp)
if inp <= 0:
    print(str(inp) + ' is OUT of range !!!')
else:
    count=0
    print('Output ==>',end=' ')
    for i in range(1,inp+1):
        if inp % i == 0:
            print (i,end =' ')
            count+=1
    print('')
    print('Total ==> '+ str(count))
