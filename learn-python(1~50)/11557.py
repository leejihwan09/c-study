T = int(input())
r = {}
for i in range(T):
    N = int(input())
    for k in range(N):
        m,h = map(str,input().split())
        if m in r:
            r.update({m:int(h)})
        else:
            r[m]=int(h)
    print(max(r,key=r.get))