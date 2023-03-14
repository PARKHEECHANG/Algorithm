def row_check(row, st, ed):
    pd_range = (ed - st + 1) // 2  # 회문 반복 수
    for i in range(pd_range):
        if lst[row][st + i] != lst[row][ed - i]:
            return 0
    return ed - st + 1  # 회문 길이

def col_check(col, st, ed):
    pd_range = (ed - st + 1) // 2  # 회문 반복 수
    for i in range(pd_range):
        if lst[st + i][col] != lst[ed - i][col]:
            return 0
    return ed - st + 1  # 회문 길이
for t_case in range(10) :

    t_num = int(input())
    lst = [ list(map(str, input())) for i in range(100) ]
    maxx = 0
    print(f'#{t_num}', end=' ')
    
    # 행검사
    for line in range(100) :

        for st in range(100) : # 회문 시작점
            for ed in range(100) : # 회문 끝점
                if st > 99-ed : # 시작점이 더 크면 다음 열
                    break
                if lst[line][st] == lst[line][99-ed] : # 행 검사
                    val = row_check(line, st, 99-ed)
                    if val > maxx :
                        maxx = val
                if lst[st][line] == lst[99-ed][line] : # 열 검사
                    val = col_check(line, st, 99-ed)
                    if val > maxx :
                        maxx = val

    print(maxx)