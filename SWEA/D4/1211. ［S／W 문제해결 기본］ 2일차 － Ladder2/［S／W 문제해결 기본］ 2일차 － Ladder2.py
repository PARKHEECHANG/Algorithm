def ladder(y, x) :

    visited = [ [0 for i in range(100)] for i in range(100) ]
    cnt = 0 # 움직인 횟수
    dy = [0,0,1]
    dx = [-1,1,0]

    while 1 :
        if y == 99 :
            return cnt

        for i in range(3) :
            ny = dy[i] + y
            nx = dx[i] + x

            if 0 <= ny < 100 and 0 <= nx < 100 : # 범위 안
                if lst[ny][nx] == 1 and visited[ny][nx] == 0 : # 다리이면서 방문한 적이 없으면
                    visited[ny][nx] = 1
                    y = ny
                    x = nx
                    cnt += 1

for t_case in range(10) :

    t_num = int(input())
    lst = [ list(map(int, input().split())) for i in range(100) ]

    minn = 21e8

    for i in range(100) :
        if lst[0][i] == 1 : # 시작점
            cnt = ladder(0, i)
            if cnt < minn : # 적은 움직임
                minn = cnt
                min_start = i

    print(f'#{t_num} {min_start}')