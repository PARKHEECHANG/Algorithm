from collections import deque

ladder_cnt, snake_cnt = map(int, input().split())
board = [ 0 for i in range(101) ] # 사다리, 뱀 판단
dice_result = [ 0 for i in range(101) ] # 주사위 횟수 저장

for i in range(ladder_cnt) :
    ladder_f, ladder_e  = map(int, input().split())
    board[ladder_f] = ladder_e
    
for i in range(snake_cnt) : 
    snake_f, snake_e = map(int, input().split())
    board[snake_f] = snake_e

deq = deque()

deq.append(1)

while deq :
    
    x = deq.popleft()
    for dice in range(1,7) :
        now = x + dice
        if 1 <= now <= 100 : # 범위 안 
            if board[now] == 0 : # 사다리, 뱀이 없으면
                if dice_result[now] == 0 : # 방문 안 했으면
                    dice_result[now] = dice_result[x] + 1
                    deq.append(now) # 주사위 이동

            elif board[now] != 0 : # 사다리, 뱀이 있으면
                if dice_result[board[now]] == 0 : # 방문 안 했으면
                    dice_result[board[now]] = dice_result[x] +1 # 주사위 횟수 가져가기
                    deq.append(board[now]) # 순간 이동

print(dice_result[100])