n, l = map(int, input().split()) # 신호등의 개수, 도로의 길이

lst = [ [0] * 3 ] + [ list(map(int, input().split())) for i in range(n) ] # 앞 칸 padding
# lst[i][0] : 신호등 위치, lst[i][1] : 빨간불 시간 lst[i][2] : 초록불 시간
# 신호등은 D가 증가하는 순서로 주어진다.
# 같은 위치에 있는 신호등이 두 개 이상 있는 경우는 없다.

t = 0 # 현재 시간
p = 0 # 현재 위치

for i in range(1, n+1) :
    p += lst[i][0]-lst[i-1][0] # 신호등 간 거리 이동
    t += lst[i][0]-lst[i-1][0] # 신호등 간 걸린 시간

    r = lst[i][1] # 빨간 신호 시간
    g = lst[i][2] # 초록 신호 시간

    light_info = t % (r  + g)
    # 현재 시간에 신호등 신호주기 나눈 나머지 : 신호 상태
    # 남은시간이 0 ~ 빨간 신호시간(0~r) :  빨간 신호
    # 남은시간이 빨간신호 종료 ~ 초록 신호시간(r~r+g) : 초록 신호

    if light_info < r : # 빨간불
        t += r - light_info # 대기시간 추가
    else : # 초록불
        continue # 통과

# 신호등 다 지난 후
t += l-p # 남은 거리 만큼 이동
print(t)