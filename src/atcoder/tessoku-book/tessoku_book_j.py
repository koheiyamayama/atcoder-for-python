n = int(input())
a = list(map(int, input().split()))
d = int(input())
lr = [list(map(int, input().split())) for _ in range(d)]

l_to_r = [0 for _ in range(n)]
l_to_r[0] = a[0]
for i in range(1, n):
    l_to_r[i] = max(l_to_r[i-1], a[i])

r_to_l = [0 for _ in range(n)]
r_to_l[-1] = a[-1]
for i in reversed(range(0, n-1)):
    r_to_l[i] = max(r_to_l[i+1], a[i])

for s in lr:
    l = s[0]
    r = s[1]
    print(max(l_to_r[l-2], r_to_l[r]))
