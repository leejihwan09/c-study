d = list(map(int,input().split()))
d.remove(max(d))
d.remove(min(d))
print(d[0])