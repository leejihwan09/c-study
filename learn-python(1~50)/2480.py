a,b,c = map(int,input().split())
money=0
if (a==b==c):
    money = money + 10000 + (a*1000)
elif (a==b):
    money = money + 1000 + (a*100)
elif (b==c):
    money = money + 1000 + (b*100)
elif (a==c):
    money = money + 1000 + (c*100)
else:
    money = money + max(a,b,c)*100
print(money)