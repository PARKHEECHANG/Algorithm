# 색종이가 도화지 밖으로 나가는 경우는 없다.
# 도화지 끝에 걸칠 수 있으며, j+1을 이용하므로 범위를 한 칸 padding
arr = [ [0] * 101 for _ in range(101) ]
n = int(input())

for i in range(n) :
    x, y = map(int, input().split())

    for i in range(y, y+10) :
        for j in range(x, x+10) :
            arr[i][j] = 1

area = 0
for i in range(100) :
    for j in range(100) :

        # 가로 검사
        if arr[i][j] == 0 and arr[i][j+1] == 1 : # 다른 색깔 즉, 경계면이면
            area += 1
        elif arr[i][j] == 1 and arr[i][j+1] == 0 :
            area += 1
        # 세로 검사
        if arr[j][i] == 0 and arr[j+1][i] == 1 :
            area += 1
        elif arr[j][i] == 1 and arr[j+1][i] == 0 :
            area += 1

print(area)