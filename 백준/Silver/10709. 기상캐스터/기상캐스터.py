def find(y, x) :
    for i in range(x,-1,-1) : # 현재 하늘 위치에서 앞으로
        if arr[y][i] == 'c' : # 구름이 있으면
            return x-i # 현재위치 - 구름위치 => 구름이 오는 시간(한 칸에 1)
        elif i == 0: # 끝까지 갔는데 구름이 없으면
            return -1 # -1 리턴
        elif arr[y][i] == '.' : continue # 하늘이면 더 앞으로

h, w = map(int,input().split())
arr = [ list(input().strip()) for _ in range(h) ]
ans = [ [0]*w for i in range(h) ]
for i in range(h) :
    for j in range(w-1,-1,-1) : # 뒤에서부터 찾기
        if arr[i][j] == 'c' : # 구름이면 움직일 필요 없음 => 0
            ans[i][j] = 0
        elif arr[i][j] == '.' : # 하늘이면 앞에 구름있는지 찾기
            ans[i][j] = find(i, j)

for i in range(h) :
    print(*ans[i])
