print('------------')
print(' Pattern-32')
print('------------')
def pattern1(n):
 for i in range(0,n):
    for j in range(0,i+1):
        print(chr(j+65),end='')
    print()
n=int(input())
pattern32(n)


