def min(ls,index):
    temp=ls[index]
    if index+1 >= len(ls):
        return temp
    mn=min(ls,index+1)
    if mn <= temp:
        return mn
    elif mn > temp:
        return temp 
inp= input('Enter Input : ').split(' ')
for i in range(len(inp)):
   inp[i]=int(inp[i])
print('Min : {0}'.format(min(inp,0)))