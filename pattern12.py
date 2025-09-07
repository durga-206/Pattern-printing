print('------------')
print(' Pattern-12 ')
print('------------')
def pattern12(n):
 for i in range(0,n):
    for space in range(0,n-i-1):
        print(' ',end='')
    for star in range(0,i+1):
        print('*',end=' ')
    print()
 for i in range(0,n):
    for space in range(0,i):
        print(' ',end='')
    for star in range(0,n-i):
        print('*',end=' ')
    print()
n=int(input())
pattern12(n)
