lis = list(map(int, input('Enter Your List : ').split()))
ans = []
if(len(lis)<=2):
    print('Array Input Length Must More Than 2')
else:
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            for k in range(j+1,len(lis)):
                temp=[]
                if(lis[i]+lis[j]+lis[k]==5):
                    temp.append(lis[i])
                    temp.append(lis[j])
                    temp.append(lis[k])
                    temp.sort()
                if(len(temp)>0 and temp not in ans):
                    ans.append(temp)
    print(ans)
