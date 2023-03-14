t = int(input())

for t_case in range(1, t+1) :

    n = int(input()) # n일 동안 듣기
    week = list(map(int, input().split()))

    minn = 21e8 # 최소 출석 일수

    # 시작 요일
    start_day = 0
    for i in range(len(week)) :
        if week[i] == 1 :
            start_day = i

        lesson = 0  # 수업 받은 일수
        day = 0  # 출석 일수

        while 1 :

            for j in range(start_day, len(week)) :
                if week[j] == 1 : # 수업 일때만 증가
                    lesson += 1
                day += 1 # 날마다 증가
                if lesson == n:
                    break
            if lesson == n:
                break
            start_day = 0  # 다음 주는 월요일


        if minn > day :
            minn = day

    print(f'#{t_case} {minn}')