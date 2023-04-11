import bisect

n = int(input())
a = list(map(int, input().split()))
q = int(input())
x = [int(input()) for _ in range(q)]

a.sort()

for i in x:
    # 第一引数の配列内でi以下の最も近いインデックス値を返す
    # bisect_rightはi上の最も近いインデックス値を返す
    ans = bisect.bisect_left(a, i)
    print(ans)
