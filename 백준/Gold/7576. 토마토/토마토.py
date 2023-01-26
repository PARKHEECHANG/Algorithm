from collections import deque


box_x_size, box_y_size = map(int, input().split()) # 박스 사이즈

tomato_box = [] # 토마토 박스
visited = [[0 for i in range(box_x_size)] for i in range(box_y_size)] # 방문 정보

for i in range(box_y_size) : # 토마토 박스 입력
        tomato_box.append( list(map(int, input().split())) )

# 모두 익었을 경우
isripe = True # 익었는가?
for y in range(box_y_size) :
    for x in range(box_x_size) :
        if tomato_box[y][x] == 0 : # 하나라도 안익었으면
            isripe = False # 안익었다
if isripe == True : # 다 익었으면
    print("0") # '0' 출력, 종료
    exit()

# 시작점 찾기
deq = deque()

for y in range(box_y_size) :
    for x in range(box_x_size) :
        if tomato_box[y][x] == 1 : # 익은 토마토 위치
            visited[y][x] = 1 # 방문 판정
            deq.append(y) # 덱에 넣기
            deq.append(x)

# 토마토 익는 방향
move_y = [-1, 1, 0 ,0]
move_x = [0, 0, -1 ,1]

# 토마토 익기
while deq :
    y = deq.popleft()
    x = deq.popleft()

    for i in range(4) : # 익은 토마토의 영향
        now_y =  y + move_y[i]
        now_x =  x + move_x[i]

        if 0 <= now_y < box_y_size and 0 <= now_x < box_x_size : # 박스 사이즈 안이면서
            if visited[now_y][now_x] == 0 and tomato_box[now_y][now_x] != -1 : # 방문한 적이 없고, 토마토가 안들어있는게 아니면
                visited[now_y][now_x] = 1
                tomato_box[now_y][now_x] = tomato_box[y][x] + 1 # 주변 토마토 익는 날짜 = 현재 토마토 익는 날짜 + 1
                deq.append(now_y)
                deq.append(now_x)

# 익지 못하는 상황
isripe = True # 익었는가?
for y in range(box_y_size) :
    for x in range(box_x_size) :
        if tomato_box[y][x] == 0 : # 안익은게 있다면
            isripe = False

if isripe == False : # 익지 못하는 상황
    print("-1") # "-1" 출력, 종료
    exit()

# 다 익는데 걸리는 날짜
max = 0
for y in range(box_y_size) :
    for x in range(box_x_size) :
        if tomato_box[y][x] > 0 : # 없거나(0) 안익은(-1) 토마토가 아니면
            if tomato_box[y][x] > max : 
                max = tomato_box[y][x]

print(max-1) # 익은 토마토 위치가 0이 아닌 1로 시작하므로 -1하기