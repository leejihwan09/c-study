a = []
for i in range(9):
    b = int(input())
    a.append(b)
print(f'{max(a)}\n{a.index(max(a))+1}')