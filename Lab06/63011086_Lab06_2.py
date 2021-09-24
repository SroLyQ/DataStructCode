
def length(txt):     
    #Code Hereasdf
    temp=txt[-1:]
    if temp == '':
        return [temp,0]
    nextText=length(txt[0:-1])
    cnt=nextText[1]+1;
    if cnt%2==0:
        temp+='~'
    else:
        temp+='*'
    nextText[0]+=temp
    return [nextText[0],cnt]

inp=input("Enter Input : ")
print("{0}\n{1}".format(length(inp)[0],length(inp)[1]),sep="")