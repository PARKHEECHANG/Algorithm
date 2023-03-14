def dfs(lv, st) :

    if lv == m:
        print(*path)
        return

    for i in range(st, n+1) :
        path[lv] = i
        dfs(lv+1, i)
        path[lv] = 0


n, m = map(int, input().split())
path = [0] * m

dfs(0, 1)