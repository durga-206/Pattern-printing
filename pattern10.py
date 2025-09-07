print('------------')
print(' Pattern-10 ')
print('------------')
def pattern10(n):
 for i in range(0,n):
    if i<=n/2:
        for j in range(0,i+1):
            print('*',end=' ')
        print()
    if i>=n/2:
        for j in range(0,n-i):
            print('*',end=' ')
        print()
n=int(input())
pattern10(n)      
