print('------------')
print(' Pattern-21')
print('------------')
n=int(input())
for i in range(0,n):
    for space in range(1,n-i):
        print(' ',end='')
    for alpha in range(0,2*i+1):
        print(chr(i+65),end='')
    print()
n=int(input())
pattern36(n)


