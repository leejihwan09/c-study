N,K = map(int,input().split())
T = []
c=0
for i in range(N):
    T.append(int(input()))
T.reverse()
while K!=0:
    for i in T:
        while K>=i:
            c+=K//i
            K%=i
print(c)