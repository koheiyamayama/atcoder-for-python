a, b = map(int, input().split())

flag = False
for i in range(a, b+1):
    if 100 % i == 0:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
