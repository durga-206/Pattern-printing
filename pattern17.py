print('------------')
print(' Pattern-17 ')
print('------------')
def pattern17(n):
 value=0
 for i in range(0,n):
    for j in range(0,i+1):
        value=1+value
        print(value,end=' ')
    print()
n=int(input())
pattern17(n)  
