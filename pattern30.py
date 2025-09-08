print('------------')
print(' Pattern-30 ')
print('------------')
def pattern30(n):
 for i in range(0,n):
    for space in range(1,n-i):
        print(' ',end='')
    for star in range(0,i+1):
        if i==0 or i==star or star==0:
         print('*',end='')
        else:
            print(' ',end='')
    print()
 for i in range(n-2,-1,-1):
    for space in range(1,n-i):
        print(' ',end='')
    for star in range(0,i+1):
        if i==0 or i==star or star==0:
           print('*',end='')
        else:
            print(' ',end='')
    print()
n=int(input())
pattern30(n)


