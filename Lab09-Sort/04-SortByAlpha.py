def sortAlp(lis):
    sort_lis=[]
    for i in lis:
        for ch in i:
            if ch.isalpha():
                sort_lis.append([i,ch])
    for i in range(len(sort_lis)):
        for j in range(len(sort_lis)):
            if j+1 < len(sort_lis) and sort_lis[j][1] > sort_lis[j+1][1]:
                temp = sort_lis[j]
                sort_lis[j]=sort_lis[j+1]
                sort_lis[j+1]=temp
    return sort_lis

inp=input('Enter Input : ').split()
sorted_inp=sortAlp(inp)
for i in sorted_inp:
    print(i[0],end=' ')
#932c 832u32 2344b