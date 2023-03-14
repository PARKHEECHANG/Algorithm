def bfs(y, x) :
    global isPass

    for i in range(4) :
        ny = dy[i] + y
        nx = dx[i] + x

        if 0 <= ny < 100 and 0 <= nx < 100 :
            if visited[ny][nx] == 0 and arr[ny][nx] == 0 :
                visited[ny][nx] = 1
                q.append(ny)
                q.append(nx)
            elif arr[ny][nx] == 3 :
                isPass = 1
                return

dy = [-1,0,1,0]
dx = [0,1,0,-1]

q = []

for t_case in range(1, 11) :

    t_num = int(input())
    arr = [ list(map(int, input().rstrip())) for i in range(100) ]

    visited = [ [0 for i in range(100)] for i in range(100) ]

    isPass = 0
    visited[1][1] = 1

    q.append(1)
    q.append(1)

    while q :
        y = q.pop()
        x = q.pop()
        bfs(y,x)

    print(f'#{t_num} {isPass}')