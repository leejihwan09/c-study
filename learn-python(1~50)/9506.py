while True:
    a=[]
    b=[]
    n = int(input())
    if n==-1:
        break
    for i in range(n-1):
        if i!=0 and n%i==0:
            a.append(i)
    if sum(a) == n:
        print(n,end=' = ',)
        for i in range(len(a)-1):
            print(a[i],end=' + ')
        print(a[-1])
    else:
        print(n,end=' is NOT perfect.\n')