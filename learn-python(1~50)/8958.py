for i in range(int(input())):
    b=0
    u=0
    a=list(str(input()))
    for j in range(len(a)):
        if a[j]=='O' and j==0:
            u+=1
            b+=1
        elif a[j]==a[j-1] and a[j]=='O' and j!=0:
            u+=1
            b+=u
        elif a[j]=='O' and j!=0:
            u+=1
            b+=1
        else:
            u=0
    print(b)
