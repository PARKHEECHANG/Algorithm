arr = [ [0]*1001 for _ in range(1001) ]
n = int(input())
for i in range(n) :
    a, b, w, h = map(int, input().split())
    papaer_num = i + 1 # 색종이 번호 (1부터 시작 + 0이 아닌 경우 조사)
    x = a
    y = 1000-b # 거꾸로 시작

    # !색종이가 격자 경계 밖으로 나가는 경우는 없다.
    for j in range(y, y-h, -1) :
        for k in range(x, x+w) :
            arr[j][k] = papaer_num

area = [0] * (n+1)
for j in range(1001) :
    for k in range(1001) :
        if arr[j][k] != 0 :
            color = arr[j][k]
            area[color] += 1

for j in range(1, n+1) :
    print(area[j])

