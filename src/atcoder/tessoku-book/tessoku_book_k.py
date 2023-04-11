n, x = map(int, input().split())
a = list(map(int, input().split()))

l = 0
r = n - 1
while True:
    m = (l+r)//2
    if x < a[m]:
        r = m - 1
    elif x > a[m]:
        l = m + 1
    else:
        print(m+1)
        break
