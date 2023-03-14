t = int(input())
for t_case in range(1, t+1) :
    lst = list(map(int, input().strip()))

    clap = lst[0] # 0명일 때 박수하는 사람

    employ_cnt = 0 # 고용인원

    for i in range(1, len(lst)) :
        if i <= clap : # i번째로 박수하는 사람 조건 충족
            clap += lst[i] # lst[i]만큼 박수하는 사람 증가
        elif i > clap : # i번째로 박수하는 사람 조건 미충족
            need_clap = i - clap # 필요한 인원
            clap += need_clap # 고용 후 박수하는 사람
            employ_cnt += need_clap # 고용 인원
            clap += lst[i] # 따라 박수하는 사람 증가

    print(f'#{t_case} {employ_cnt}')