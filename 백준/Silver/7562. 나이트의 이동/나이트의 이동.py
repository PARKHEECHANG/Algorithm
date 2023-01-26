from collections import deque

result = []

t = int(input())

for i in range(t) :
    size = int(input()) # 체스판 사이즈

    board = [[0 for i in range(size)] for i in range(size)] # 체스판 생성
    visited = [[0 for i in range(size)] for i in range(size)] # 방문 확인판

    y, x = map(int, input().split()) # 시작 좌표
    goal_y, goal_x = map(int, input().split()) # 목표 좌표

    # 나이트의 이동
    # 왼쪽 위부터 시계 방향으로
    knight_move_y_lst = [-1, -2, -2, -1, 1, 2,  2,  1]
    knight_move_x_lst = [-2, -1,  1,  2, 2, 1, -1, -2] 

    deq = deque()
    visited[y][x] = 0
    deq.append(y)
    deq.append(x)

    while deq :

        now_y = deq.popleft() # 현재 좌표 값 추출
        now_x = deq.popleft()

        if now_y == goal_y and now_x == goal_x : # 목표 지점 도달
            result.append(board[now_y][now_x]) # 결과 리스트에 좌표 값 저장
            break

        for i in range(8) : # 나이트의 이동 경우의 수
            move_y = now_y + knight_move_y_lst[i]
            move_x = now_x + knight_move_x_lst[i]
            
            if( 0 <= move_x < size and 0 <= move_y < size) : # 범위는 체스판 안
                if( visited[move_y][move_x] == 0 ) : # 방문한 적이 없으면
                    visited[move_y][move_x] = 1 # 방문 체크
                    board[move_y][move_x] = board[now_y][now_x] + 1 # 이동 좌표 값 = 현재 좌표 값 + 1
                    deq.append(move_y) # 이동 좌표 값으로 다시 시작
                    deq.append(move_x)

for i in result : # 결과 리스트 출력
    print(i)