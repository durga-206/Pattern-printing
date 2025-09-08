print('------------')
print(' Pattern-31 ')
print('------------')
def pattern31(n):
 for i in range(0,n):
    for j in range(0,i+1):
        print(chr(i+65),end='')
    print()
n=int(input())
pattern31(n)


