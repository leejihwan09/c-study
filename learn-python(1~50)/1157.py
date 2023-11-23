a=list(input())
b={}
f=[]
for i in a:
    try:
        b[i.upper()]+=1
    except:
        b[i.upper()]=1
for c,d in b.items():
    if d == max(b.values()):
        f.append(d)
if len(f)>=2:
    print('?')
else:
    print(max(b,key=b.get))