def dfs(lv) :

    if lv == m:
        print(*path)
        return

    for i in range(1, n+1) :
        path[lv] = i
        dfs(lv+1)
        path[lv] = 0

n, m = map(int, input().split())
visited = [0] * (n+1)
path = [0] * m

dfs(0)