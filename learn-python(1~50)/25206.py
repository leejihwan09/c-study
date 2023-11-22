a={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0,"P":0.0}
b=[]
c=0
for i in range(20):
    q,w,e=input().split()
    q=str(q)
    w=float(w)
    e=str(e)
    if e!='P':
        b.append(w*a[e])
        c+=w
print(format(sum(b)/c,'.6f'))