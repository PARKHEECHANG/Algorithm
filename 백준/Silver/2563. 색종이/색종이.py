paper_cnt = int(input()) # 색종이의 수

arr = [ [0] * 100 for i in range(100)] # 도화지 배열

for i in range(paper_cnt) :
    x, y = map(int, input().split())

    # arr[x][y] ~ arr[x+10][y+10]
    for i in range(x, x+10) :
        for j in range(y, y+10) :
            arr[i][j] = 1 # 색종이 영역 칠하기

area = 0 # 너비
for i in range(100) :
    for j in range(100) :
        if arr[i][j] == 1 : # 칠해진 부분 카운트
            area += 1

print(area)