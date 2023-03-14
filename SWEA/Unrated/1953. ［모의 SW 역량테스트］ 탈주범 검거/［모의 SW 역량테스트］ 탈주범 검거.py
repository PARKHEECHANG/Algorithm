def search(type) :
    if type == 1 :
        direct = [0,1,2,3]
    elif type == 2 :
        direct = [0,1]
    elif type == 3 :
        direct = [2,3]
    elif type == 4 :
        direct = [0,3]
    elif type == 5 :
        direct = [1,3]
    elif type == 6 :
        direct = [1,2]
    elif type == 7 :
        direct = [0,2]
 
    return direct
 
def CanGoNear(d, next) :
    if d == 0 : # 상, 위쪽 터널 타입 1, 2, 5, 6
        if next == 1 or next == 2 or next == 5 or next == 6 :
            return True
    elif d == 1 : # 하, 아래쪽 터널 타입 1, 2, 4, 7
        if next == 1 or next == 2 or next == 4 or next == 7 :
            return True
    elif d == 2 : # 좌, 왼쪽 터널 타입 1, 3, 4, 5
        if next == 1 or next == 3 or next == 4 or next == 5 :
            return True
    elif d == 3 : # 우, 오른쪽 터널 타입 1, 3, 6, 7
        if next == 1 or next == 3 or next == 6 or next == 7 :
            return True
    else : # 다른 터널 타입이면 False
        return False
 
# def bfs(y, x) :
 
 
t = int(input())
for t_case in range(1, t+1) :
 
    # 세로 크기, 가로 크기, 맨홀 위치y, 맨홀 위치x, 탈출 소요 시간
    size_y, size_x, st_y, st_x, time = map(int, input().split())
    type = [ list(map(int,input().split())) for i in range(size_y) ]
    visit = [ [0 for i in range(size_x)] for i in range(size_y) ]
 
    q = []
    q.append([st_y, st_x])
    visit[st_y][st_x] = 1
 
        # 상 하 좌 우
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
 
    while q :
        y, x = q.pop()
 
        # 터널 타입에 따라 사용할 수 있는 방향 배열 가져오기
        direct_lst = search(type[y][x])
 
        for i in range(len(direct_lst)):
            d = direct_lst[i]  # [2, 3]
            ny = y + dy[d]
            nx = x + dx[d]
 
            # 범위 조건
            if 0 <= ny < size_y and 0 <= nx < size_x:
 
                # 갈 수 있는 '주변'터널 타입 조사
                if CanGoNear(d, type[ny][nx]):
 
                    if visit[ny][nx] == 0 or visit[ny][nx] > visit[y][x] + 1 :
                        visit[ny][nx] = visit[y][x] + 1
                        q.append([ny, nx])
 
    cnt = 0 # 탈주범이 위치할 수 있는 장소의 수
    for y in range(size_y) :
        for x in range(size_x) :
            if 0 < visit[y][x] <= time :
                cnt += 1
 
    print(f'#{t_case} {cnt}')
 
'''
1. 범위 조건
2. 방문 조건 : 방문 0 or 더 빨리 갈 수 있음
3. 터널 조건 (방향에 따른 타입)
    y-1 = 1,2,5,6
    y+1 = 1,2,4,7
    x-1 = 1,3,4,5
    x+1 = 1,3,6,7
'''