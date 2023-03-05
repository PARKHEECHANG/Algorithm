l = int(input()) # 롤 케이크 길이
n = int(input()) # 방청객의 수

lst = [0] * (l+1) # 케이크 - 방청객 번호 저장

# [1] 많은 조각을 기대하는 방청객 번호 구하기
need_cake = 0 # 원하는 케이크 개수
for i in range(n) :
    lsnr = i + 1 # 방청객 1번 부터 입력
    st, ed = map(int, input().split()) # 원하는 케이크 첫 조각 ~ 마지막 조각

    if ed - st + 1 > need_cake : # 더 많은 케이크를 원하는 방청객이 있으면
        # 여러 명인 경우 번호가 작은 사람 출력, '>=' 가아닌 '>'로 하면 된다.
        need_cake = ed-st+1
        wish_lsnr = lsnr

    for j in range(st, ed+1) : # 케이크에 방청객 번호 입력
        if lst[j] == 0 : # 이미 적혀있는 번호는 줄 수 없다.
            lst[j] = lsnr

# [2] 실제로 많은 조각을 받는 방청객 번호
dat = [0] * (n+1)
for i in range(1, l+1) : # 케이크에 방청객 번호 카운트
    dat[lst[i]] += 1

mx_idx = 1
for i in range(1, n+1) :
    if dat[i] > dat[mx_idx] :
        mx_idx = i

print(wish_lsnr)
print(mx_idx)