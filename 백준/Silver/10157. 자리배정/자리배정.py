def move(d, y, x) :
    d = d
    y = y
    x = x
    
    for i in range(k-1) : # k-1번 이동 (이미 1번에서 시작)
        visit[y][x] = 1
        # d=0 : up, d=1 : right, d=2 : down, d=3 : left
        if d == 0:  # 위로 이동
            if y - 1 < 0 or visit[y - 1][x] == 1:  # 위로 이동하다 막히면
                # 오른쪽 이동
                d = 1
                x += 1
                continue
            else:  # 안막히면
                y -= 1
                continue

        elif d == 1:  # 오른쪽 이동
            if x + 1 > size_x - 1 or visit[y][x + 1] == 1:  # 오른쪾 이동하다 막히면
                # 아래 이동
                d = 2
                y += 1
                continue
            else:  # 안막히면
                x += 1
                continue

        elif d == 2:  # 아래 이동
            if y + 1 > size_y - 1 or visit[y + 1][x] == 1:  # 아래 이동하다 막히면
                # 왼쪽 이동
                d = 3
                x -= 1
                continue
            else:  # 안막히면
                y += 1
                continue

        elif d == 3:  # 왼쪽 이동
            if x - 1 < 0 or visit[y][x - 1] == 1:  # 왼쪽 이동하다 막히면
                # 위 이동
                d = 0
                y -= 1
                continue
            else:  # 안막히면
                d = 3
                x -= 1
                continue        
        
    # k번째에 좌표 출력
    print(x+1, size_y-y)
    return

size_x, size_y =  map(int, input().split())
k = int(input())

arr = [ [0]*size_x for _ in range(size_y) ]
visit = [ [0]*size_x for _ in range(size_y) ]

if size_y * size_x < k : # 좌석 번호 없음
    print(0)
else :
    # move(방향, y위치, x위치)
    move(0, size_y-1, 0)
