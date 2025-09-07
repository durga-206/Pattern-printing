print('------------')
print(' Pattern-8 ')
print('------------')
def pattern8(n):
 for i  in range(0,n):
    for space in range(0,i):
        print(' ', end=' ')
    for star in range(2*n-1,2*i,-1):
        print('*',end=' ')
    print()
n=int(input())
pattern8(n)

