def bfs(y, x) :

    # 초기 조건
    q = []
    q.append((y, x))
    visited[y][x] = 1
    tmp_room = arr[y][x] # 처음에 출발해야 하는 방 번호
    cnt = 1 # 최대 몇 개의 방을 이동

    while q :
        y, x = q.pop(0)

        # 방향 리스트보다 튜플을 활용하는 것이 메모리 부담이 적다. (Python!)
        for dy, dx in ( (-1,0), (1, 0), (0, -1), (0, 1) ) :
            ny, nx = y + dy, x + dx

            if 0 > ny or ny >= n or 0 > nx or nx >= n : continue
            if visited[ny][nx] == 1 : continue
            if abs(arr[y][x] - arr[ny][nx]) != 1 : continue
            cnt += 1
            visited[ny][nx] = 1
            q.append((ny, nx))
            if tmp_room > arr[ny][nx] : # 다음 방이 더 작은 방 번호라면
                tmp_room = arr[ny][nx]

    return tmp_room, cnt

t = int(input())
for t_case in range(1, t+1) :

    n = int(input())
    arr = [ list(map(int, input().split())) for _ in range(n) ]
    visited = [ [0] * n for i in range(n) ]

    max_cnt = 0
    ans = 0
    for i in range(n) :
        for j in range(n) :
            if visited[i][j] == 0 : # 미리 방문 체크하면 탐색 범위 줄어들어 좋다
                tmp_room, cnt = bfs(i, j)

                if max_cnt < cnt : # 최대 이동 수
                    max_cnt = cnt
                    ans = tmp_room
                elif max_cnt == cnt and ans > tmp_room : # 최대 이동 수가 같으면, 번호가 작은 방
                    ans = tmp_room

    print(f'#{t_case} {ans} {max_cnt}')

