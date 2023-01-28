size = int(input())
arr = [ list(map(int, input().split())) for _ in range(size)]

width = 0 # 가로 타입
length = 1 # 세로 타입
diagonal = 2 # 대각선 타입

cnt = 0

def dfs(y, x, type) :
    global cnt

    if y == size-1 and x == size-1 :
        cnt += 1
        return
    
    if type == width  or type == diagonal : # 가로 이동
        if x+1 < size and arr[y][x+1] == 0 :
            dfs(y, x+1, width)

    if type == length or type == diagonal : # 세로 이동
        if y+1 < size and arr[y+1][x] == 0 :
            dfs(y+1, x, length)
    
    if y+1 < size and x+1 < size : # 대각선 이동
        if arr[y][x+1] == 0 and arr[y+1][x] == 0 and arr[y+1][x+1] == 0 :
            dfs(y+1, x+1, diagonal)

dfs(0, 1, width)
print(cnt)