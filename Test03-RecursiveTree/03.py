def printPy(n,level):
    if(level > n):
        return
    else:
        print('^'*(n-level),end='')
        print('#'*((2*(level-1))+1),end='')
        print('^'*(n-level),end='')
        print('')
    printPy(n,level+1)
inp = int(input('Enter Input : '))
if inp <= 0:
    print('Not Draw!',end='')
printPy(inp,1)