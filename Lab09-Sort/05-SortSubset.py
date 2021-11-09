def findSubset(val,nowVal,arr,path):
    global subSet
    if arr == []:
        return
    nowVal += arr[0]
    if nowVal > val:
        path.append(arr[0])
        findSubset(val,nowVal,arr[1:],path)
        path.pop()
        findSubset(val,nowVal-arr[0],arr[1:],path)
    elif nowVal < val:
        path.append(arr[0])
        findSubset(val,nowVal,arr[1:],path)
        path.pop()
        findSubset(val,nowVal-arr[0],arr[1:],path)
    elif nowVal == val:
        path.append(arr[0])
        temp=path.copy()
        subSet.append(temp)
        findSubset(val,nowVal,arr[1:],path)
        path.pop()
        findSubset(val,nowVal-arr[0],arr[1:],path)
    return 

def sortSubset(arr):
    for lis in arr:
        for j in range(len(lis)):
            for idx in range(len(lis)):
                if idx + 1 < len(lis) and lis[idx]>lis[idx+1]:
                    temp=lis[idx]
                    lis[idx]=lis[idx+1]
                    lis[idx+1]=temp
    for i in arr:
        for j in range(len(arr)):
            if j+1 < len (arr) and len(arr[j])>len(arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
            elif j+1 < len (arr) and len(arr[j])==len(arr[j+1]):
                idx = 0
                while idx < len(arr[j]) and arr[j][idx] == arr[j+1][idx]:
                    idx+=1
                if arr[j][idx] > arr[j+1][idx]:
                    temp = arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp
    for i in arr:
        print(i)
                    
val,inp=input('Enter Input : ').split('/')
inp = [int(e) for e in inp.split()]
subSet=[]
findSubset(int(val),0,inp,[])
#print(subSet)
if subSet==[]:
    print('No Subset')
else:
    sortSubset(subSet)
#print(subSet)