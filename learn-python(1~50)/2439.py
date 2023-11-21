a = int(input())
for i in range(a+1):
    if i!=0:
        for j in range(a-i):
            print(" ",end='')
        for l in range(i):
            print("*",end='')
        print()