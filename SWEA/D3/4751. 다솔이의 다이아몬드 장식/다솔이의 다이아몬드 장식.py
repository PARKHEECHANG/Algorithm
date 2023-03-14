t = int(input())

def diamond(y, x) :
    # 시계 방향
    dy = [-2,-1,0,1,2,1,0,-1]
    dx = [0,1,2,1,0,-1,-2,-1]

    for i in range(8) :
        ny = dy[i] + y
        nx = dx[i] + x
        arr[ny][nx] = '#' # 다이아 씌우기

for t_case in range(t) :

    strr = input()
    size = (len(strr)*4) + 1

    arr = [['.' for i in range(size)] for i in range(size)]

    for i in range(len(strr)) :
        arr[2][2+(i*4)] = strr[i] # 알파뱃의 위치 규칙
        diamond(2, 2+(i*4)) # 알파뱃을 기준으로

    for i in range(5) :
        print(''.join(arr[i]))