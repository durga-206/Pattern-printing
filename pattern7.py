print('------------')
print(' Pattern-7 ')
print('------------')
n=int(input())
for i in range(0,n):
    for space in range(0,n-i):
        print(' ',end=' ')
    for j in range(0,1+2*i):
        print('*',end=' ')
    print()


