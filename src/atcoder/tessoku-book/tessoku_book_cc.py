n = input().zfill(8)

sum = 0
for i in [7, 6, 5, 4, 3, 2, 1, 0]:
    u = int(n[7-i])
    sum += u * (2 ** i)

print(sum)
