def ch() :
    sm = 0
    for i in range(n) :

        cnt = 1
        for j in range(n-1) :
            if arr[i][j] == arr[i][j+1] : # 열 검사
                cnt += 1
            else :
                sm = max(sm, cnt)
                cnt = 1
                continue
        sm = max(sm, cnt)

        cnt = 1
        for j in range(n-1) :
            if arr[j][i] == arr[j+1][i] : # 행 검사
                cnt += 1
            else:
                sm = max(sm, cnt)
                cnt = 1
                continue
        sm = max(sm, cnt)

    return sm

n = int(input())
arr = [ list(input().strip()) for _ in range(n) ]

mx = 0
for i in range(n) :
    for j in range(n-1) :
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        sm = ch()
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        mx = max(mx, sm)

for i in range(n) :
    for j in range(n-1) :
        arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
        sm = ch()
        arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
        mx = max(mx, sm)

print(mx)