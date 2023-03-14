def dfs(lv) :

    if lv == m:
        print(*path)
        return

    for i in range(1, n+1) :
        if visited[i] == 1 : continue
        
        path[lv] = i
        visited[i] = 1
        
        dfs(lv+1)
        
        visited[i] = 0
        path[lv] = 0

n, m = map(int, input().split())
visited = [0] * (n+1)
path = [0] * m

dfs(0)