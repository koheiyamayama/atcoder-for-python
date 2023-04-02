n, k = map(int, input().split())

count = 0
for r in range(1, n+1):
    for b in range(1, n+1):
        if n >= k - (r + b) >= 1:
            count += 1

print(count)
