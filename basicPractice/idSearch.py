n = int(input())
item = []
for i in range(n) :
  a=int(input())
  b={
      "index" : i+1,
      "id" : a
  }
  item.append(b)
c = int(input())
cnt=0
for i in item :
  if i.get("id") == c :
      cnt+=1
print('Position:',end=" ")
for i in item :
  if i.get("id")== c and cnt>1:
      print(str(i.get("index")),end=',')
      cnt-=1
  elif i.get("id")== c and cnt<=1:
      print(str(i.get("index")))
