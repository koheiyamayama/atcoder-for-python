h, w = map(int, input().split())
xx = [list(map(int, input().split())) for _ in range(h)]
q = int(input())
aa = [list(map(int, input().split())) for _ in range(q)]

bb = [[0]*(w+1) for i in range(h+1)]

for hh in range(1, h+1):
    for ww in range(1, w+1):
        bb[hh][ww] = bb[hh][ww-1] + xx[hh-1][ww-1]

for hh in range(1, h+1):
    for ww in range(1, w+1):
        bb[hh][ww] = bb[hh-1][ww] + bb[hh][ww]

for a in aa:
    A = a[0]
    B = a[1]
    C = a[2]
    D = a[3]
    print(bb[C][D]+bb[A-1][B-1]-bb[A-1][D]-bb[C][B-1])
