a,b=map(int,input().split())
c=list(map(int,input().split()))
while True:
    d=0
    for i in c:
        if b>=i:
            d+=1
            b+=1
            c.remove(i)
    if d==0:
        break
print(b)