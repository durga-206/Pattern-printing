print('------------')
print(' Pattern-17 ')
print('------------')
n=int(input())
value=0
for i in range(0,n):
    for j in range(0,i+1):
        value=1+value
        print(value,end=' ')
    print()
