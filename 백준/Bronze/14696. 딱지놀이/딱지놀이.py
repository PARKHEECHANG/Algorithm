n = int(input())

for i in range(n) :
    lst_A = list(map(int, input().split()))
    lst_B = list(map(int, input().split()))

    cnt = lst_A[0] # 첫 요소 == 딱지 개수
    dat_A = [0] * 5 # A의 딱지 타입 개수 저장
    for i in range(1, cnt+1) :
        type = lst_A[i]
        dat_A[type] += 1

    cnt = lst_B[0] # 첫 요소 == 딱지 개수
    dat_B = [0] * 5  # B의 딱지 타입 개수 저장
    for i in range(1, cnt+1) :
        type = lst_B[i]
        dat_B[type] += 1

    # 별 비교
    if dat_A[4] > dat_B[4] :
        print('A')
        continue
    elif dat_A[4] < dat_B[4] :
        print('B')
        continue

    # 동그라미 비교
    elif dat_A[4] == dat_B[4] :
        if dat_A[3] > dat_B[3] :
            print('A')
            continue
        elif dat_A[3] < dat_B[3] :
            print('B')
            continue

        # 네모 비교
        elif dat_A[3] == dat_B[3] :
            if dat_A[2] > dat_B[2]:
                print('A')
                continue
            elif dat_A[2] < dat_B[2]:
                print('B')
                continue
            
            # 세모 비교
            elif dat_A[2] == dat_B[2]:
                if dat_A[1] > dat_B[1]:
                    print('A')
                    continue
                elif dat_A[1] < dat_B[1]:
                    print('B')
                    continue

                elif dat_A[1] == dat_B[1] :
                    print('D')
                    continue


