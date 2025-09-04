print('------------')
print(' Pattern-33')
print('------------')
n=int(input())
for i in range(0,n):
    for j in range(0,n-i):
        print(chr(n-i+64),end='')
    print()
