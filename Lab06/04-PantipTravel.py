def pantip(k, n, arr, path):
    # Code Here
  #print('ex : '+str(path))
  temp=0
  if arr==[]:
      return
  if n+arr[0]>k and arr[0]<k:
      temppan=pantip(k,n,arr[1:],path)
      if(temppan != None):
          temp+=temppan
  elif n+arr[0]>k and arr[0] >=k:
      temppan=pantip(k,n,arr[1:],path)
      if(temppan != None):
          temp+=temppan
  elif n+arr[0]<k:
      path.append(arr[0])
      temppan=pantip(k,n+arr[0],arr[1:],path)
      if(temppan != None):
          temp+=temppan
      path.pop()
      temppan=pantip(k,n,arr[1:],path)
      if(temppan != None):
          temp+=temppan
  elif n+arr[0]==k:
      path.append(arr[0])
      temp+=1
      print(str(path).replace('[','').replace(']','').replace(',',''))
      path.pop()
      temppan=pantip(k,n,arr[1:],path)
      if(temppan!=None):
          temp+=temppan
      return temp
  return temp
inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))