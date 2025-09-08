print('------------')
print(' Pattern-33')
print('------------')
def pattern33(n):
 for i in range(0,n):
    for j in range(0,n-i):
        print(chr(n-i+64),end='')
    print()
n=int(input())
pattern33(n)


