def dfs(y, x) :
    global isPass

    for i in range(4) :
        ny = dy[i] + y
        nx = dx[i] + x

        if 0 <= ny < 16 and 0 <= nx < 16 :
            if visited[ny][nx] == 0 and arr[ny][nx] == 0 :
                visited[ny][nx] = 1
                dfs(ny, nx)
            elif arr[ny][nx] == 3 :
                isPass = True
                return

dy = [-1,0,1,0]
dx = [0,1,0,-1]

for t_case in range(1, 11) :

    t_num = int(input())
    arr = [ list(map(int, input().rstrip())) for i in range(16) ]

    visited = [ [0 for i in range(16)] for i in range(16) ]

    for i in range(16) :
        for j in range(16) :
            if arr[i][j] == 2 :
                st_y, st_x = i, j

    isPass = False
    visited[st_y][st_x] = 1
    dfs(st_y,st_x)

    if isPass == True :
        print(f'#{t_num} 1')
    elif isPass == False :
        print(f'#{t_num} 0')
