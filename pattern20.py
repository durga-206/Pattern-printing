print('------------')
print(' Pattern-20 ')
print('------------')
def pattern20(n):
 for i in range(0,n):
    for star in range(0,n-i):
        print('*',end='')
    for space in range(0,i):
        print(' ',end='')
    for space in range(0,i):
        print(' ',end='')
    for star in range(0,n-i):
        print('*',end='')
    print()
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
pattern20(n) 
