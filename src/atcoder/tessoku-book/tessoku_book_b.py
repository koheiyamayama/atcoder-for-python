# param
b, c = map(int, input().split())
a = map(int, input().split())

ans = False
for i in a:
    if i == c:
        ans = True

if ans:
    print("Yes")
else:
    print("No")
