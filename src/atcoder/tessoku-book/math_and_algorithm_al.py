t = int(input())
n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]

list = [0]*(t+1)
for i in range(n):
    l = lr[i][0]
    r = lr[i][1]

    list[l] += 1
    list[r] -= 1

acum = [0]*t
for i in range(t):
    acum[i] = acum[i-1] + list[i]

for i in range(t):
    print(acum[i])
