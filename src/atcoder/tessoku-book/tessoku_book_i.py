H, W, N = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(N)]

acum = [[0]*(W+1) for _ in range(H+1)]
for s in abcd:
    A = s[0]
    B = s[1]
    C = s[2]
    D = s[3]
    acum[A][B] += 1
    if C+1 < H+1 and D+1 < W+1:
        acum[C+1][D+1] += 1
    if D+1 < W+1:
        acum[A][D+1] -= 1
    if C+1 < H+1:
        acum[C+1][B] -= 1


for h in range(1, H+1):
    for w in range(1, W+1):
        acum[h][w] += acum[h][w-1]


for h in range(1, H+1):
    for w in range(1, W+1):
        acum[h][w] += acum[h-1][w]


for h in range(1, H+1):
    for w in range(1, W+1):
        if w != W:
            print(acum[h][w], "", end="")
        else:
            print(acum[h][w])
