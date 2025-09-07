print('------------')
print(' Pattern-16 ')
print('------------')
def pattern16(n):
 for i in range(1,n):
    for j in range(1,i+1):
        print(j,end='')
    for space in  range(1,n-i):
        print(' ',end='')
    for space in  range(1,n-i):
        print(' ',end='')
    for j in range(i,0,-1):
        print(j,end='')
    print()
n=int(input())
pattern16(n)       
        
