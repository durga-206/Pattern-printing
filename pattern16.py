print('------------')
print(' Pattern-16 ')
print('------------')
n=int(input())
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end='')
#for i in range(1,n):
    for space in  range(1,n-i):
        print(' ',end='')
    for space in  range(1,n-i):
        print(' ',end='')
    for j in range(i,0,-1):
        print(j,end='')
    print()
        
        
