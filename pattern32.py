print('------------')
print(' Pattern-32')
print('------------')
n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(j+65),end='')
    print()
