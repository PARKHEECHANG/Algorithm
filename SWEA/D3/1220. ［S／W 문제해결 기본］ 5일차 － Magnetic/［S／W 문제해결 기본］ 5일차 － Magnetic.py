def down(y, x) :
    global deadlock
 
    for i in range(y+1, n): # 다음 행이
        if arr[i][x] == 2 : # 2라면
            deadlock += 1 # 교착 상태 ++
            arr[i][x] = 0 # 합치기
            return
        else : # 1이면
            arr[i][x] = 0 # 합치기
 
for t_case in range(1, 11) :
    n = int(input())
    arr = [ list(map(int, input().split())) for _ in range(n) ]
    deadlock = 0 # 교착 상태
 
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == 1 : # 1이면 내려가기
                down(i, j)
 
    print(f'#{t_case} {deadlock}')