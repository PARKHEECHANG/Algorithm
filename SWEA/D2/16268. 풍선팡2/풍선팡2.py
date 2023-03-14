def search(y, x) :
    SUM = 0
    for dy, dx in ((-1,0),(1,0),(0,0),(0,-1),(0,1)) :
        ny, nx = dy + y, dx + x

        if ny < 0 or nx < 0 or ny >= n or nx >= m : continue
        SUM += arr[ny][nx]

    return SUM

t = int(input())
for t_case in range(1, t+1) :

    n, m = map(int, input().split())

    arr = [ list(map(int, input().split())) for i in range(n)]

    MAX = 0
    for i in range(n) :
        for j in range(m) :
            MAX = max(search(i, j), MAX)

    print(f'#{t_case} {MAX}')