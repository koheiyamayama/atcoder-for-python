n = int(input())
a = list(map(int, input().split()))
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

acum = [0]
for i in range(n):
    acum.append(acum[i]+a[i])

for query in lr:
    l = query[0]
    r = query[1]
    atari = acum[r] - acum[l-1]
    hazure = r - l + 1 - atari
    if atari > hazure:
        print("win")
    elif atari < hazure:
        print("lose")
    else:
        print("draw")
