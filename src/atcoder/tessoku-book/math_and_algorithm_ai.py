n, q = map(int, input().split())
a = list(map(int, input().split()))
lr = [list(map(int, input().split())) for _ in range(q)]

nn = [0]
for i in range(n):
    nn.append(nn[i]+a[i])

for query in lr:
    l = query[0]
    r = query[1]
    print(nn[r]-nn[l-1])
