print('------------')
print(' Pattern-22 ')
print('------------')
n=int(input())
for i in range(0,n):
    for space in range(0,n-i):
        print(' ',end='')
    for star in range(0,i+1):
        if star==0 or i==n-1 or i==star:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
