print('------------')
print(' Pattern-24 ')
print('------------')
n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
     if i==0 or j==0 or i==n-1 or i==j:
        print('*',end=' ')
     else:
         print(' ',end=' ')
    print()
n=int(input())
pattern1(n)

