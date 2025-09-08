print('------------')
print(' Pattern-29 ')
print('------------')
def pattern29(n):
 for i in range(0,n):
    for j in range(n-1,i-1,-1):
        if i==0 or i==j or j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
 for i in range(0,n):
    for j in range(0,i+1):
        if i==0 or i==n-1 or j==i or j==0:
            print('*',end='')
        else:
            print(' ',end='')
    print()
n=int(input())
pattern29(n)


