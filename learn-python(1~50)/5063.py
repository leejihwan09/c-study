for i in range(int(input())):
    a,b,c= map(int,input().split())
    if a==b-c:
        print("does not matter")
    elif a<b-c:
        print("advertise")
    else:
        print("do not advertise")