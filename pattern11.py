print('------------')
print(' Pattern-11 ')
print('------------')
n=int(input())
for i  in range(0,n):
    for space in range(0,i):
        print(' ',end='')
    for star in range(n-1,i-1,-1):
     if star==n-1 or i==0 or star==i:
        print('*',end='')
     else:
         print(' ',end='')
    print()
for i in range(1,n):
    for space in range(1,n-i):
        print(' ',end='')
    for star in range(0,i+1):
        if star==0 or i==1 or star==i or i==n-1:
            print('*',end='')
        else:
          print(' ',end='')
    print()

    
