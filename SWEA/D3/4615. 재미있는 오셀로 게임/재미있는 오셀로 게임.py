t = int(input())

def cnt() :
    w_cnt = b_cnt = 0

    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == 2 :
                w_cnt += 1
            elif arr[i][j] == 1 :
                b_cnt += 1
    return b_cnt, w_cnt

def search(now_dy, now_dx, you_y, you_x) :

    for size in range(n):
        ny = you_y + now_dy * size
        nx = you_x + now_dx * size

        if 0 <= ny < n and 0 <= nx < n :
            if arr[ny][nx] == me_color : # 자신의 색이 나오면
                for i in range(size) : # 범위만큼
                    arr[you_y + now_dy*i][you_x + now_dx*i] = me_color # 자신의 색으로 바꾸기
                return True
            elif arr[ny][nx] == you_color :
                continue
            elif arr[ny][nx] == 0 :
                return False

for t_case in range(1, t+1) :
    n, m = map(int, input().split()) # 한 변의 길이, 돌을 놓는 횟수

    arr = [ [0 for i in range(n)] for i in range(n) ]

    arr[n//2-1][n//2-1] = arr[n//2][n//2] = 2 # 백돌 초기 세팅
    arr[n//2-1][n//2] = arr[n//2][n//2-1] = 1 # 흑돌 초기 세팅

    dy = [-1,-1,-1,0,0,1,1,1]
    dx = [-1,0,1,-1,1,-1,0,1]

    for i in range(m) :
        y, x, me_color = map(int, input().split())

        if me_color == 1 :
            you_color = 2
        elif me_color == 2:
            you_color = 1

        # 1부터 시작
        y -= 1
        x -= 1

        for i in range(8) :
            # 주변에 상대 돌이 있으면서
            you_y = y + dy[i]
            you_x = x + dx[i]
            if 0 <= you_y < n and 0 <= you_x < n:
                if arr[you_y][you_x] == you_color: # 주변에 상대방 돌이 있다
                    if search(dy[i], dx[i], you_y, you_x):  # 그 다음 칸 어딘가에 자신의 색이 있다
                        arr[y][x] = me_color # 돌 놓기 가능

    b_cnt, w_cnt = cnt()

    print(f'#{t_case} {b_cnt} {w_cnt}')

# 18 통과 / 30