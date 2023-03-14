for i in range(4) :
    lst = list(map(int, input().split()))
    stx, sty, edx, edy = lst[0], lst[1], lst[2], lst[3]
    stx2, sty2, edx2, edy2 = lst[4], lst[5], lst[6], lst[7]

    # [1] 분리된 경우
    if edx < stx2  or edy < sty2 or edx2 < stx or edy2 < sty :
        print('d')
    # [2] 선분으로 겹치는 경우
    elif sty == edy2 or sty2 == edy or stx == edx2 or edx == stx2 :
        # [3] 점으로 겹치는 경우
        if (edy == sty2 and edx == stx2) or (sty == edy2 and edx == stx2) or (edy2 == sty and edx2 == stx) or (sty2 == edy and edx2 == stx) :
            print('c')
        else :
            print('b')
    else : # [4] 직사각형으로 겹치는 경우
        print('a')