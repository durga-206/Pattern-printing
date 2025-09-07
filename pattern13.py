print('------------')
print(' Pattern-13 ')
print('------------')
def pattern13(n):
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
n=int(input())
pattern13(n)
