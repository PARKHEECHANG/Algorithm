def recur(lv, n) :

    if lv == m-1 :
        print(f'#{t_case} {n}')
        return
    n = final_n*n
    recur(lv+1, n)

for t_case in range(1, 11) :
    t_num = int(input())
    final_n, m = map(int, input().split())
    recur(0, final_n)