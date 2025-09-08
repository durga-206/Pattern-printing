print('------------')
print(' Pattern-28 ')
print('------------')
n=int(input())
for i in range(0,n):
    for j in range(n-1,i-1,-1):
        if i==0 or j==n-1 or i==j:
          print("*",end='')
        else:
            print(' ',end='')
    print()
n=int(input())
pattern28(n)

