print('------------')
print(' Pattern-27 ')
print('------------')
n=int(input())
for i in range(0,n):
    for space in range(0,i):
        print(' ',end='')
    for star in range(2*n-1,2*i,-1):
        print('*',end='')
    print()
for i in range(1,n):
    for space in range(1,n-i):
        print(' ',end='')
    for star in range(0,2*i+1):
        print('*',end='')
    print()
