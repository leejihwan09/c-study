a = list(str(input()))
b=0
for i in range(len(a)):
    if i==0 and a[i]:
        b+=10
    elif a[i]==a[i-1]:
        b+=5
    else:
        b+=10
print(b)