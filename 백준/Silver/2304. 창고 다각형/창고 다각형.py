n = int(input())

arr = [0] * 1001
mx_h = 0
for i in range(n) :
    l, h = map(int, input().split())
    arr[l] = h
    mx_h = max(mx_h, h)

area = 0
now_h = 0
now = 0
mx_st = 0
for i in range(1, 1001) : # 앞에서부터 중앙
    if now_h < arr[i] :
        area += now_h * (i - now)
        now = i
        now_h = arr[i]

    if now_h == mx_h :
        mx_st = i
        break

now = 1001
now_h = 0
mx_ed = 0
for i in range(1000, 0, -1) : # 뒤에서부터 중앙
    if now_h < arr[i] :
        area += now_h * (now - i)
        now = i
        now_h = arr[i]

    if now_h == mx_h :
        mx_ed = i
        break

area += (mx_ed-mx_st+1) * mx_h # 제일 높은 기둥 너비 더하기

print(area)
