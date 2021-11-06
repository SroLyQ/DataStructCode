def natural_sum(n):
    #code here
    if n == 0:
        return 0
    x = n+natural_sum(n-1)
    if n == num:
        print(str(n),end = ' = ')
    else:
        print(str(n),end=' + ')
    return x

print(' *** Natural sum ***')
num = int(input("Enter number : ")) 
print("%.d" %(natural_sum(num)))