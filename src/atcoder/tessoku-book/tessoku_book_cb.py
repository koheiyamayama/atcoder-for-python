n = int(input())
a = list(map(int, input().split()))

flag = False
for i in range(n):
    for ii in range(i+1, n):
        for iii in range(ii+1, n):
            if a[i] + a[ii] + a[iii] == 1000:
                flag = True
                break

if flag:
    print("Yes")
else:
    print("No")
