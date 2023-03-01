t = int(input())
for t_case in range(1, t+1) :
    final_n = int(input()) # 상수 n ()
    n = final_n
    dat = [0] * 10

    cnt = 1
    while 1 :
        flag = True
        n = str(n)
        for i in range(len(n)) :
            dat[int(n[i])] = 1

        for i in range(10) :
            n = int(n)
            if dat[i] == 0 :
                n += final_n
                cnt += 1
                flag = False
                break

        if flag == True :
            print(f'#{t_case} {n}')
            break
