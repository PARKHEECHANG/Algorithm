A, B = map(int, input().split())

cnt = 1

while (True) :
    if A == B :
        print(cnt)
        break

    if B < A :
        print("-1")
        break

    if B % 10 == 1 :
        B = B // 10
        cnt += 1

    elif B % 2 == 0 :
        B = B // 2
        cnt += 1

    elif B % 2 == 1 :
        print("-1")
        break