a = list(map(int, input().split()))
b = list(map(int, input().split()))
c=0
for i in range(9):
    if int(a[i])>int(b[i]):
        c+=1

if c>=1 and sum(a)<sum(b):
    print("Yes")
else:
    print("No")