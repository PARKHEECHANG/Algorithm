def find(y, x) :
    for i in range(x,-1,-1) :
        if arr[y][i] == 'c' :
            return x-i
        elif i == 0:
            return -1
        if arr[y][i] == '.' : continue

h, w = map(int,input().split())
arr = [ list(input().strip()) for _ in range(h) ]
ans = [ [0]*w for i in range(h) ]
for i in range(h) :
    for j in range(w-1,-1,-1) :
        if arr[i][j] == 'c' :
            ans[i][j] = 0
        elif arr[i][j] == '.' :
            ans[i][j] = find(i, j)

for i in range(h) :
    print(*ans[i])
