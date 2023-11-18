t = input()
score_1 = 100
score_2 = 100
for i in range(int(t)):
    a,b = map(int,input().split())
    if a>b:
        score_2 = score_2 - a
    if b>a:
        score_1 = score_1 - b
print(f'{score_1}\n{score_2}')