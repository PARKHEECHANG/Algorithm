t = int(input())
 
def get_service_size(k) : # 방범 영역
    global dy
    global dx
    dy = []
    dx = []
 
    # 위~가운데 방범
    for y in range(0, -k, -1) :
        for x in range(-k+1-y, k+y) :
            dy.append(y)
            dx.append(x)
 
    # 가운데 다음 칸 ~ 아래 방범
    for y in range(1, k) :
        for x in range(-k+1+y, k-y) :
            dy.append(y)
            dx.append(x)
 
def check(y, x, size) : # size == 운영 비용 == 방향 배열 크기
    house_cnt = 0 # 집 개수
 
    for i in range(size) :
        ny = y + dy[i]
        nx = x + dx[i]
         
        if 0 <= ny < n and 0 <= nx < n : # if 범위 안
            if arr[ny][nx] == 1 : # if 집
                house_cnt += 1 # ++
     
    if (house_cnt * m) >= size : # if 손해 없음
        return house_cnt
    else :
        return 0
 
for t_case in range(1, t+1) :
    # 5 ≤ N ≤ 20, 1 ≤ M ≤ 10
    n, m = map(int, input().split()) # 도시의 크기, 한 집 비용
    arr = [ list(map(int, input().split())) for i in range(n) ]
 
    # 운영 비용(DP)
    k = [0] * (n+2)
    k[1] = 1
    k[2] = 5
    '''
    # 도시 최대 크기 20*20 = 400
    # 점화식 k 최대 크기
    k = 3, 13
    k = 4, 25
    k = 5, 41
    k = 6, 61
    k = 7, 85
    k = 8, 113
    k = 9, 145
    k = 10, 181
    k = 11, 221
    k = 12, 265
    k = 13, 313
    k = 14, 365
    k = 15, 421
    k = 16, 481
    k = 17, 545
    k = 18, 613
    k = 19, 685
    k = 20, 761
    k = 21, 841
    '''
    maxx_house_cnt = 0
    for i in range(1, n+2): # 1~n+1
        if i == 1 :
            k[1] = 1
        elif i == 2 :
            k[2] = 5
        else :
            k[i] = k[i - 1] + (4 * (i - 1))
 
            # k[i] : 운영 비용
        get_service_size(i) # 방범 사이즈 설정
 
        for y in range(n) : # k가 1,2,3..일 때 방범 한 칸 한 칸 검사
            for x in range(n) :
                house_cnt = check(y, x, k[i]) # 좌표y, 좌표x, 방향 배열 사이즈
                if house_cnt > maxx_house_cnt :
                    maxx_house_cnt = house_cnt
 
    print(f'#{t_case} {maxx_house_cnt}')
