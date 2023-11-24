c=0
d=[]
for i in range(4):
    a,b = map(int,input().split())
    c-=a
    c+=b
    d.append(c)
print(max(d))