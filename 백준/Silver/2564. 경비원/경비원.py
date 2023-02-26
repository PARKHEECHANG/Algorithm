width, height = map(int, input().split()) # 가로 길이, 세로 길이

n = int(input()) # 상점의 개수
lst = [0]  * n # 상점 리스트

for i in range(n) :
    lst[i] = list(map(int, input().split()))

dong_p, dong_x = map(int, input().split()) # 동근이의 위치, 동근이의 거리

summ = 0

for i in range(n) :
    shop_p = lst[i][0] # 상점 위치
    shop_x = lst[i][1] # 상점 거리

    if shop_p == dong_p: # 같은 위치
        summ += abs(dong_x-shop_x) # 거리 차이

    # 평행 위치
    elif (shop_p == 1 and dong_p == 2) or (shop_p == 2 and dong_p == 1) : # 남북 평행
        forward = height + (width - dong_x) + (width - shop_x)  # 시계방향
        reverse = height + dong_x + shop_x  # 반시계방향
        summ += min(forward, reverse)

    elif (shop_p == 3 and dong_p == 4) or (shop_p == 4 and dong_p == 3) :  # 동서 평행
        forward = width + (height - dong_x) + (height - shop_x)  # 시계방향
        reverse = width + dong_x + shop_x  # 반시계방향
        summ += min(forward, reverse)

    # 수직 위치
    elif shop_p == 1 : # 상점이 북쪽
        if dong_p == 3 : # 동근이 서쪽
            summ += shop_x + dong_x # 북서 수직
        elif dong_p == 4 : # 동근이 동쪽
            summ += (width - shop_x) + dong_x # 북동 수직

    elif shop_p == 2 : # 상점이 남쪽
        if dong_p == 3 : # 동근이 서쪽
            summ += shop_x + (height - dong_x) # 남서 수직
        elif dong_p == 4 : # 동근이 동쪽
            summ += (width - shop_x) + (height - dong_x) # 남동 수직

    elif shop_p == 3 : # 상점이 서쪽
        if dong_p == 1 : # 동근이 북쪽
            summ += shop_x + dong_x # 서북 수직
        elif dong_p == 2 : # 동근이 남쪽
            summ += (height - shop_x) + dong_x # 서남 수직

    elif shop_p == 4 :  # 상점이 동쪽
        if dong_p == 1 : # 동근이 북쪽
            summ += shop_x + (width - dong_x)  # 동북 수직
        elif dong_p == 2:  # 동근이 남쪽
            summ += (height - shop_x) + (width - dong_x) # 동남 수직

print(summ)