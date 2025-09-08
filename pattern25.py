print('------------')
print(' Pattern-25 ')
print('------------')
def pattern25(n):
 for i in range(0,n):
    for j in range(0,i+1):
        print('*',end=' ')
    print()
 for i in range(0,n-1):
    for j in range(0,n-1-i):
        print('*',end=' ')
    print()
n=int(input())
pattern25(n)


