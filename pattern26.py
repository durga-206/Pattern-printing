print('------------')
print(' Pattern-26 ')
print('------------')
def pattern25(n):
 for i in range(0,n):
    for space in range(1,n-i):
        print(' ',end='')
    for star in range(0,i+1):
        print('*',end='')
    print()
 for i in range(0,n):
    for space in range(0,i+1):
        print(' ',end='')
    for j in range(0,n-i-1):
        print('*',end='')
    print()
n=int(input())
pattern26(n)


