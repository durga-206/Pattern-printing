print('------------')
print(' Pattern-21 ')
print('------------')
def pattern21(n):
 for i in range(0,n):
    for j in range(0,n):
        if i==0 or j==0 or i==n-1 or j==n-1:
          print(n-1,end='')
        elif i==0+1 or j==0+1 or i==n-2 or j==n-2:
            print(n-2,end='')
        elif i==0+2 or j==0+2 or i==n-3 or j==n-3:
            print(n-3,end='')
        else:
            print(' ',end='')
    print()
n=int(input())
pattern21(n)


