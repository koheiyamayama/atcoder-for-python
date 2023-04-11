N = int(input())

acum = [[0]*1501 for _ in range(1501)]
for i in range(N):
    a, b, c, d = map(int, input().split())
    # acum[b][a] += 1
    # acum[d+1][c+1] += 1
    # acum[d+1][a] -= 1
    # acum[b][c+1] -= 1
    acum[b][a] += 1
    acum[d][c] += 1
    acum[d][a] -= 1
    acum[b][c] -= 1

# for i in range(10):
#     print(acum[i][0:10])

for y in range(0, 1501):
    for x in range(0, 1501):
        if x-1 >= 0:
            acum[y][x] = acum[y][x] + acum[y][x-1]

for y in range(0, 1501):
    for x in range(0, 1501):
        if y-1 >= 0:
            acum[y][x] = acum[y][x] + acum[y-1][x]

# for i in range(10):
#     print(acum[i][0:10])

count = 0
for y in range(0, 1501):
    for x in range(0, 1501):
        if acum[y][x] >= 1:
            count += 1

print(count)
