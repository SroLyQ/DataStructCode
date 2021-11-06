def odd_list(al):
   l2=[]
   for a in al:
       if(a%2==1):
           l2.append(a)
   return l2

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)