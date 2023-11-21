a = int(input())
list = list(map(int,input().split()))
list2 = []
for i in list:
    list2.append(i/max(list)*100)
b = sum(list2)/a
print(b)
