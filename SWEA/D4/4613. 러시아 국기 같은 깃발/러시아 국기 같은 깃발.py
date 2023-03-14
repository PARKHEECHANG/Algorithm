# 경우의 수
# W, B, R
# W => 1~n-2
# B => 2~n-1
# R => 3~n

# W 1 - B 1 - R n-2
# W 1 - B 2 - R n-3
#....
# W 2 - B 1 - R n-3
# W 2 - B 2 _ R n-4

def change_W(st, ed):
    cnt = 0
    for i in range(st, ed) :
        for j in range(m) :
            if arr[i][j] != 'W' :
                cnt += 1
    return cnt

def change_B(st, ed):
    cnt = 0
    for i in range(st, ed):
        for j in range(m):
            if arr[i][j] != 'B':
                cnt += 1
    return cnt

def change_R(st, ed):
    cnt = 0
    for i in range(st, ed):
        for j in range(m):
            if arr[i][j] != 'R':
                cnt += 1
    return cnt

t = int(input())
for t_case in range(1, t+1) :

    n, m = map(int, input().split())
    arr = [ list(input()) for i in range(n) ]

    ans = 21e8
    for w in range(n-2) :
        for b in range(w+1, n-1) :
            cnt = change_W(0, w+1)
            cnt += change_B(w+1, b+1)
            cnt += change_R(b+1, n)

            ans = min(cnt, ans)

    print(f'#{t_case} {ans}')