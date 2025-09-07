print('------------')
print(' Pattern-6 ')
print('------------')
def pattern6(n):
 for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
n=int(input())
pattern6(n)
