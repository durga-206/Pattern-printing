print('------------')
print(' Pattern-2 ')
print('------------')
def pattern2(n):
 for i in range(1,n+1):
    for j in range(i):
        print('*', end=' ')
    print()
n=int(input())
pattern2(n)
