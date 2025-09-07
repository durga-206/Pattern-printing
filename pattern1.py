print('------------')
print(' Pattern-1 ')
print('------------')
def pattern1(n):
 for i in range(0,n):
    for j in range(0,n):
        print('*',end=' ')
    print()
n=int(input())
pattern1(n)
