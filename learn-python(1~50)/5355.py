a = int(input())
for i in range(a):
    b = list(map(str,input().split()))
    b[0] = float(b[0])
    for i in range(len(b)-1):
        if (b[i+1]=='@'):
            b[0]*=3
        elif (b[i+1]=='%'):
            b[0]+=5
        elif (b[i+1]=='#'):
            b[0]-=7
    print(f'{b[0]:0.2f}')