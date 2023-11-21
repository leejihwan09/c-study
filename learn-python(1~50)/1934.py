for i in range(int(input())):
    a,b = map(int,input().split())
    g=a
    m=b
    d=0
    r=0
    while True:
        d=a%b
        if d==0:
            break
        r=b
        b=d
        a=r
    print(round(g*m/b))