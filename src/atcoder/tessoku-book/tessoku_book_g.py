d = int(input())
n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]

list = [0]*(d+1)
for i in range(n):
    l = lr[i][0]
    r = lr[i][1]

    list[l-1] += 1
    list[r] -= 1


acum = [0]*d
for i in range(d):
    acum[i] = list[i] + acum[i-1]

for i in range(d):
    print(acum[i])
