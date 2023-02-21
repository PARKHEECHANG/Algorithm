arr = [ list(map(int, input().split())) for i in range(5) ]
call = [ list(map(int, input().split())) for i in range(5) ]

def search() : # 빙고 검사
    bingo = 0 # 빙고 개수

    for i in range(5) :
        col_check = 0  # 열 체크 개수
        row_check = 0  # 행 체크 개수

        for j in range(5) :
            if arr[i][j] == 0 :
                row_check += 1
            if arr[j][i] == 0 :
                col_check += 1
        if col_check == 5 :
            bingo += 1
        if row_check == 5 :
            bingo += 1

    diag_check = 0  # 왼쪽 대각선 체크 개수
    diag2_check = 0  # 오른쪽 대각선 체크 개수
    for i in range(5) :
        if arr[i][i] == 0 :
            diag_check += 1
        if arr[i][4-i] == 0 :
            diag2_check += 1
    if diag_check == 5 :
        bingo += 1
    if diag2_check == 5 :
        bingo += 1

    return bingo

def find(value) :
    for i in range(5) :
        for j in range(5) :
            if value == arr[i][j] :
                arr[i][j] = 0

call_cnt = 0 # 사회자가 부른 수
breaker = False # 이중 for문 빠져나오기

for i in range(5) :
    for j in range(5) :
        call_cnt += 1 # 사회자가 부른 수 ++
        find(call[i][j]) # 빙고판 찾고 체크
        cnt = search() # 빙고 검사

        if cnt >= 3 :
            print(call_cnt)
            breaker = True
            break
    if breaker : break
