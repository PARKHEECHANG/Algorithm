def move(d) : # 방향 d를 입력받음
    d_lst = ((0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1))
    # 방향       R       L       B        T        RT       LT       RB       LB
    global kx, ky, sx, sy

    dy = d_lst[d][0] # 해당 방향에 y
    dx = d_lst[d][1] # 해당 방향에 x

    if ky + dy < 0 or kx + dx < 0 or ky + dy >= 8 or kx + dx >= 8 : return # 왕이 끝에 있으면
    if ky + dy == sy and kx + dx == sx : # 돌이 있으면
        if sy + dy < 0 or sx + dx < 0 or sy + dy >= 8 or sx + dx >= 8 : return # 돌이 끝에 있으면
        else : # 돌 이동 후 왕 이동
            sy = sy + dy
            sx = sx + dx
            ky = ky + dy
            kx = kx + dx
    else: # 돌이 없으면
        # 왕만 이동
        ky = ky + dy
        kx = kx + dx

arr = [ [0] * 8 for _ in range(8) ]
kp, sp, n = map(str, input().split())

kx = ord(kp[0])-65 # 킹 x
ky = 8-int(kp[1]) # 킹 y 

sx = ord(sp[0])-65 # 돌 x
sy = 8-int(sp[1]) # 돌 y

for i in range(int(n)) :
    command = input() # 명령 입력

    if command == 'R' :
        move(0)
    elif command == 'L' :
        move(1)
    elif command == 'B' :
        move(2)
    elif command == 'T' :
        move(3)
    elif command == 'RT' :
        move(4)
    elif command == 'LT' :
        move(5)
    elif command == 'RB' :
        move(6)
    elif command == 'LB' :
        move(7)

print(f'{chr(kx+65)}{8-ky}')
print(f'{chr(sx+65)}{8-sy}')