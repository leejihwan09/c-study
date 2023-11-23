b=0
input()
for i in list(map(int,input().split())):
    c=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                c+=1
        if c==0:
            b+=1
print(b)