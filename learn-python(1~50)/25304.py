a=int(input())
b=0
for i in range(int(input())):
    c,d=map(int,input().split())
    b+=c*d
if b==a:
    print("Yes")
else:
    print("No")