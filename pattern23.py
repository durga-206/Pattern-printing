print('------------')
print(' Pattern-23 ')
print('------------')
n=int(input())
for i in range(0,n):
    for space in range(0,i):
        print(' ',end='')
    for star in range(n-1,i-1,-1):
        if i==0 or star==0 or i==star or star==n-1:
          print('*' ,end=' ')
        else:
            print(' ',end=' ') 
    print()
