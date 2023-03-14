def fun(st_y,st_x,ed_y,ed_x) :
    for i in range(st_y, ed_y) :
        for j in range(st_x, ed_x) :
            arr[i][j] = 1

arr = [ [0 for i in range(100)] for i in range(100) ]

for i in range(4) :
    st_y, st_x, ed_y, ed_x = map(int, input().split())
    fun(st_y, st_x, ed_y, ed_x)

cnt = 0
for i in range(100) :
    for j in range(100) :
        if arr[i][j] == 1 :
            cnt += 1

print(cnt)