import sys
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[ 0 for i in range(m)] for i in range(n)]

move_y = [-1,1,0,0]
move_x = [0,0,-1,1]

deq = deque([])
visited[0][0] = 1

def bfs(y, x) :
    deq.append(y)
    deq.append(x)
    while deq :
        y = deq.popleft()
        x = deq.popleft()

        for i in range(4) :
            ny = y + move_y[i]
            nx = x + move_x[i]

            if(0 <= nx < m  and 0 <= ny < n) :
                if(visited[ny][nx] == 0 and arr[ny][nx] == 1) :
                    visited[ny][nx] = 1
                    arr[ny][nx] = arr[y][x] + 1
                    deq.append(ny)
                    deq.append(nx)

bfs(0,0)
print(arr[n-1][m-1])