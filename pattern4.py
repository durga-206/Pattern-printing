print('------------')
print(' Pattern-4 ')
print('------------')
def pattern4(n):
 for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
n=int(input())
pattern4(n)
