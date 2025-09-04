print('------------')
print(' Pattern-15 ')
print('------------')
n=int(input())
for i in range(0,n):
    for star in range(0,n-i):
        print("*",end='')
    for space in range(0,i):
        print(' ',end="")
    for space in range(0,i):
        print(' ',end="")
    for star in range(0,n-i):
        print('*',end='')
    print()
