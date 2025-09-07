print('------------')
print(' Pattern-9 ')
print('------------')
def pattern9(n):
 for i in range(0,n):
    for space in range(1,n-i):
        print(' ',end='')
    for star in range(0,1+2*i):
        print('*',end='')
    print()
 for i in range(0,n):
    for space in range(1,i+1):
        print(' ',end='')
    for star in range(2*n-1,2*i,-1):
        print('*',end='')
    print()
n=int(input())
pattern9(n)
