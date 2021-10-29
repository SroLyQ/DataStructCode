import timeit
from itertools import permutations


def print_table():
    for row in range(n):
        print(table[row])

def put_queen(x,y):
    if table[y][x] == 0:
        for m in range(n):
            table[y][m] = 1
            table[m][x] = 1
            table[y][x] = 2
            if y+m <= n-1 and x+m <= n-1:
                table[y+m][x+m] = 1
            if y-m >= 0 and x+m <= n-1:
                table[y-m][x+m] = 1
            if y+m <= n-1 and x-m >= 0:
                table[y+m][x-m] = 1
            if y-m >= 0 and x-m >= 0:
                table[y-m][x-m] = 1
        return True
    else:
        return False
for n in range(2,17):
    start = timeit.default_timer()
    print('N='+str(n))
    table = [[0]*n for _ in range(n)]    
    perms = permutations([int(i) for i in range(n)])


    num_comb = 0

    for perm in perms:
        c=0
        for i in range(n):
            if put_queen(perm[i],i) == True:
               c+=1
            else:
                break
            if c==n:
                #print_table()
                num_comb += 1
                #print(f"solution{num_comb}")
                #print(" ")
        table = [[0] * n for _ in range(n)]
    print('number of sol: '+str(num_comb))
    stop = timeit.default_timer()
    print('Time use: ', stop - start)