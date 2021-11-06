def asteroid_collision(asts,idx):
    if idx == -1:
        return asts
    temp=asteroid_collision(asts,idx-1)
    nowAst=temp[idx]
    if nowAst > 0 and idx < len(temp)-1:
        newAst = temp[idx+1]
        if newAst < 0:
            if abs(newAst) < nowAst:
               temp[idx+1]=nowAst
               temp[idx]=0
               temp = asteroid_collision(temp,idx+1)
            elif abs(newAst) > nowAst:
                temp[idx] = newAst
                temp[idx+1]=0
                temp = asteroid_collision(temp,idx)
            else:
                temp[idx]=0
                temp[idx+1]=0
        if newAst==0:
            temp[idx+1]=nowAst
            temp[idx]=0
            temp=asteroid_collision(temp,idx+1)
    if nowAst < 0 and idx > 0:
        newAst = temp[idx-1]
        if newAst > 0:
            if abs(nowAst) < newAst:
                temp[idx]=newAst
                temp[idx-1]=0
                temp = asteroid_collision(temp,idx)
            elif abs(nowAst) > newAst:
                temp[idx-1]=nowAst
                temp[idx]=0
                temp = asteroid_collision(temp,idx-1)
            else:
                temp[idx]=0
                temp[idx-1]=0
        if newAst==0:
            temp[idx-1]=nowAst
            temp[idx]=0
            temp=asteroid_collision(temp,idx-1)
    return temp
x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(str(asteroid_collision(x,len(x)-1)).replace(' 0,','').replace('[0, ','[').replace(', 0]',']').replace('[0]','[]'))
