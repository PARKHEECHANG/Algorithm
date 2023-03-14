t = int(input())
for t_case in range(1, t+1) :
    print(f'#{t_case}',end=' ')
    arr = [ list(input().strip()) for _ in range(5) ]
 
    mx_idx = 0
    for i in range(len(arr)) :
        for j in range(len(arr[i])) :
            mx_idx = max(mx_idx, j)
    col = 0
    while 1 :
 
        if col > mx_idx :
            break
 
        for i in range(5) :
            if len(arr[i])-1 < col :
                continue
            print(arr[i][col],end='')
 
        col += 1
    print()