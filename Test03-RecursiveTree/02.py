def findMax(array,mx):
    if(len(array)==0):
        return mx
    if array[0]>mx:
        mx = array[0]
    return findMax(array[1:],mx)

inp=[int(e) for e in input('Enter Input : ').split()]
findMax(inp,inp[0])
print('Max : ' + str(findMax(inp,inp[0])))