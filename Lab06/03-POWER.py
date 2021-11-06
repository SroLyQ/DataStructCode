def POW(a,b):
    if a==0:
        return 0
    if b==0:
        return 1
    return a*POW(a,b-1)
a,b=input('Enter Input a b : ').split(' ')
a=int(a)
b=int(b)
print(POW(a,b))