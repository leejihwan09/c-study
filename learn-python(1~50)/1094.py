x = int(input())
c = 0
n = 64
while x>0:
    if n>x:
        n=n/2
    else:
        c+=1
        x-=n
print(c)