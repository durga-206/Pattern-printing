print('------------')
print(' Pattern-13 ')
print('------------')
n=int(input())
for i in range(0,n):
    for star in range(0,i+1):
        print('*',end='')
    for space in range(1,n-i):
        print(' ',end='')
    for space in range(1,n-i):
        print(' ',end='')
    for star in range(0,i+1):
        print('*',end='')
    print()

