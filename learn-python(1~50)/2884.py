H,M = map(int,input().split())
if M-45<0:
    M=M-45
    M=60+M

    if H!=0:
        H-=1
    else:
        H+=23
else:
    M-=45
print(H,M)