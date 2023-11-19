T = int(input())
O = 0
for i in range(T):
    for i in range(9):
        Y,K = map(int,input().split())
        O = O + Y-K
    if (O<0):
        print("Korea")
    elif (O>0):
        print("Yonsei")
    else:
        print("Draw")