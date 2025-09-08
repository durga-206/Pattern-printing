print('------------')
print(' Pattern-35')
print('------------')
n=int(input())
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(chr(64+j),end='')
    print()
n=int(input())
pattern35(n)
