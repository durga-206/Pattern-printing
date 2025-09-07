print('------------')
print(' Pattern-14 ')
print('------------')
def pattern14(n):
 for i in range(0,n):
    for j in range(0,n-i):
        print('*',end='')
    print()
 for i in range(0,n-1):
    for j in range (0,i+2):
        print('*',end='')
    print()
n=int(input())
pattern14(n)
