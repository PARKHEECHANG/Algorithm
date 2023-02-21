def get_max(up, down): # 위, 아래를 제외한 옆면 중 가장 큰 값 저장

    dat = [0] * 7  # up, down 체크
    dat[up] = dat[down] = 1
    for i in range(6, 0, -1):  # 6~1 큰 수부터 검사
        if dat[i] == 0:  # 옆면이면
            return i # 남은 옆면 중 큰 수 리턴

def search_across(i): # 반대편 인덱스 찾기
    # A[0] - F[5] /  B[1] - D[3] / C[2] - E[4]

    # 주사위 경우의 수
    if i == 0:
        across_idx = 5

    if i == 1 or i == 2:
        across_idx = i + 2

    if i == 3 or i == 4:
        across_idx = i - 2

    if i == 5:
        across_idx = 0

    return across_idx

def next_dice(dice, now_idx) : # 닿는 면(같은 숫자) 찾기
    for i in range(6) :
        if arr[dice+1][i] == arr[dice][now_idx] : # 다음 주사위랑 같은 숫자이면
            return i # 그 숫자 인덱스 리턴


n = int(input())  # 주사위 개수
arr = [list(map(int, input().split())) for i in range(n)]

maxx = 0 # 최댓값

for i in range(6) : # 첫 주사위 면 선택
    # 시작점 1, 2, 3, 4, 5, 6 마다 경우의 수
    now = arr[0][i] # 한 면 선택
    across_idx = search_across(i) # 반대편 추출
    across = arr[0][across_idx]
    summ = get_max(now, across) # 두 면을 제외한 => 옆면(그 중 큰 수) 추출

    for j in range(n-1) :
        now_idx = next_dice(j, across_idx)  # 다음 주사위 idx <= 현재 주사위 번호, 현재 주사위 인덱스

        now = arr[j+1][now_idx] # 다음 주사위 값
        across_idx = search_across(now_idx)
        across = arr[j+1][across_idx] # 다음 주사위 맞은 편 값

        summ += get_max(now, across) # 두 면을 제외한 => 옆면(그 중 큰 수) 추출

    if summ > maxx :
        maxx = summ

print(maxx)
