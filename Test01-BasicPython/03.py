print(' *** Recite the multiplication table ***')
inp = input('Enter pattern for child 1 to 3 (-1 for sep) : ').split(' -1 ')
inp[2]=inp[2].split(' -1')
print('')
print('Pattern for child 1 : ' + inp[0])
print('Pattern for child 2 : ' + inp[1])
print('Pattern for child 3 : ' + inp[2][0])
child1=inp[0].split(' ')
child2=inp[1].split(' ')
child3=inp[2][0].split(' ')
day=1
i=0
found=False
while day <= 365:
    if(child1[i%len(child1)] == child2[i%len(child2)] == child3[i%len(child3)]):
        print('They recite same multiplication table in '+str(day)+' days')
        found=True
        break
    i+=1
    day+=1
if not found:
    print('This year they never recite same multiplication table !!!')