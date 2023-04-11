n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
abcd = [list(map(int, input().split())) for _ in range(q)]

tdg = [[0]*(1501) for _ in range(1501)]
for p in xy:
    tdg[p[1]][p[0]] += 1

for y in range(1501):
    for x in range(1501):
        tdg[y][x] = tdg[y][x-1] + tdg[y][x]

for y in range(1501):
    for x in range(1501):
        tdg[y][x] = tdg[y-1][x] + tdg[y][x]

for s in abcd:
    A = s[0]
    B = s[1]
    C = s[2]
    D = s[3]

    print(tdg[D][C] + tdg[B-1][A-1] - tdg[B-1][C] - tdg[D][A-1])
