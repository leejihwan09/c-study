N = int(input())
U = []
for i in range(N):
    U.append(0)

for i in range(N):
    a,b,c = map(int,input().split())
    if (a==b and b==c):
        U[i]=10000+(a*1000)
    elif (a==b):
        U[i]=1000+(a*100)
    elif (b==c):
        U[i]=1000+(b*100)
    elif (a==c):
        U[i]=1000+(c*100)
    else:
        U[i]=max(a,b,c)*100
print(max(U))

