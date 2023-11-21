while True:
    a,b = map(int,input().split())
    if a!=0 and b!=0 and a>b:
        print("Yes")
    elif a!=0 and b!=0:
        print("No")
    else:
        break