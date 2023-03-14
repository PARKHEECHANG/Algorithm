def check(y, x) :
    global flag
    dy = [1,1,1,0]
    dx = [-1,0,1,1]

    for i in range(4) : # 방향배열
        omok = 1 # 연속 수
        for j in range(1, 5) : # dy[i], dx[i] 방향으로 뻗어가기
            ny = y + (dy[i] * j) 
            nx = x + (dx[i] * j)
            if ny < 0 or nx < 0 or ny >= n or nx >= n : # 범위 벗어나면 오목 초기화
                break
            if arr[ny][nx] != 'o' : # 돌이 아니면 오목 초기화
                break
            omok += 1 # 나머지는 o
            if omok == 5 : # 오목
                flag = True

t = int(input())
for t_case in range(1, t+1) :

    n = int(input()) # n개
    arr = [ list(input().strip()) for _ in range(n) ]

    flag = False
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == 'o' : # 돌이 있으면
                check(i, j) # 오목 검사

    if flag == True :
        print(f'#{t_case} YES')
    else :
        print(f'#{t_case} NO')