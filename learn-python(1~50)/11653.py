b=a = int(input())
i=0
while i < a+1:
    if i!=0 and i!=1 and b%i==0:
        b=b/i
        print(i)
        i=0
    i+=1