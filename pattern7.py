print('------------')
print(' Pattern-7 ')
print('------------')
def pattern7(n):
 for i in range(0,n):
    for space in range(1,n-i):
        print(' ',end=' ')
    for j in range(0,1+2*i):
        print('*',end=' ')
    print()
n=int(input())
pattern7(n)

