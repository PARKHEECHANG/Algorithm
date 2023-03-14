pwd_lst = ['0001101','0011001','0010011','0111101','0100011',
            '0110001','0101111','0111011','0110111','0001011']

def search_st(n, m) :
    for i in range(n) :
        for j in range(m-1,-1,-1) : # 뒤에서부터 검사
            if arr[i][j] == '1' :
                return i, j

t = int(input())
for t_case in range(1, t+1) :
    n, m = map(int, input().split())

    arr = [ list(input().strip()) for _ in range(n) ]

    y, x = search_st(n, m)

    ans = []
    while 1 :
        for num in range(10) :
            if ''.join(arr[y][x-6:x+1]) == pwd_lst[num] :
                ans.append(int(num))
                x -= 7
        if len(ans) == 8 :
            break

    odd = 0
    even = 0
    for i in range(7,-1,-1) : # 뒤에서부터 넣었으니, 거꾸로 확인
        if (8-i) % 2 == 0 :
            even += ans[i]
        elif (8-i) % 2 == 1 :
            odd += ans[i]

    if ( (odd*3) + even ) % 10 == 0 :
        print(f'#{t_case} {sum(ans)}')
    else :
        print(f'#{t_case} 0')