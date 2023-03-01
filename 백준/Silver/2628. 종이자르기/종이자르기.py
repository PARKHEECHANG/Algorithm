width, length = map(int, input().split()) # 가로, 세로

sero = [0, width] # 세로로 자르는 것은 x축으로 구분하는 것을 뜻함.
garo = [0, length] # 가로로 자르는 것은 y축으로 구분하는 것을 뜻함.

n = int(input())
for i in range(n) :
    flag, num = map(int, input().split())

    if flag == 0 : # 가로 구분자 추가
        garo.append(num)
    elif flag == 1: # 세로 구분자 추가
        sero.append(num)

max_area = 0
garo.sort()
sero.sort()

# 뒤에서 부터 나눠서 사각형 너비 구하기
for i in range(len(garo)-1, 0, -1) :
    for j in range(len(sero)-1, 0, -1) :
        area = 0 # 너비
        area = (garo[i] - garo[i-1]) * (sero[j] - sero[j-1])
        if area > max_area :
            max_area = area

print(max_area)