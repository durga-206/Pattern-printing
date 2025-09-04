print('------------')
print(' Pattern-10 ')
print('------------')
n=int(input())
for i in range(0,n):
    if i<=n/2:
        for j in range(0,i+1):
            print('*',end=' ')
        print()
    if i>=n/2:
        for j in range(0,n-i):
            print('*',end=' ')
        print()
      
