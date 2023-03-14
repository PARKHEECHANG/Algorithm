def ladder(y, x) :
    visited = [[0 for i in range(100)] for i in range(100)]

    while(True) :
        if board[y][x] == 2 :
            return True
        elif y == 99 :
            return False

        dy = [0,0,1]
        dx = [-1,1,0]

        for i in range(3) :
            ny = y+dy[i]
            nx = x+dx[i]

            if 0 <= ny < 100 and 0 <= nx < 100 :
                if visited[ny][nx] == 0:
                    if board[ny][nx] == 1 or board[ny][nx] == 2 :
                        visited[ny][nx] = 1
                        y = ny
                        x = nx

result = []

for t in range(10) :
    n = int(input())
    board = [ list(map(int, input().split())) for i in range(100)]

    for start in range(100) :
        if board[0][start] :
            if ladder(0, start) :
                result.append(start)

for i in range(10) :
    print(f'#{i+1} {result[i]}')