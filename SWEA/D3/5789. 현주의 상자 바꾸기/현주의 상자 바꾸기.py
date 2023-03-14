t = int(input())
for t_case in range(1, t+1) :

    n, q = map(int, input().split()) # n개의 상자, q회 변경

    arr = [0] * (n+1) # 1~n번

    for i in range(1, q+1) :
        l, r = map(int, input().split())
        for j in range(l, r+1) :
            arr[j] = i

    print(f'#{t_case}', end=' ')
    for i in range(1, n+1) :
        print(arr[i], end=' ')
    print()