T = int(input())
a =0
b=0
c=0
while True:
    if T>=300:
        T-=300
        a+=1
    else:
        break
while True:
    if T>=60:
        T-=60
        b+=1
    else:
        break
while True:
    if T%10==0 and T>=10:
        T-=10
        c+=1
    elif T==0:
        print(a,b,c)
        break
    else:
        print(-1)
        break
