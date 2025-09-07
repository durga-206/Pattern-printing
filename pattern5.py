print('------------')
print(' Pattern-5 ')
print('------------')
def pattern5(n):
 for i in range(n,0,-1):
    for i in range(i):
        print('*' ,end=' ')
    print()
n=int(input())
pattern5(n)
