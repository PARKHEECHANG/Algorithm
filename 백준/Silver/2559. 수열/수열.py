n, k = map(int, input().split())
lst = list(map(int, input().split()))

p = 0
sm = 0
for i in range(p, p+k) :
    sm += lst[i]

mx = sm
for i in range(n-k) :
    sm -= lst[i]
    sm += lst[i+k]

    mx = max(sm, mx)

print(mx)