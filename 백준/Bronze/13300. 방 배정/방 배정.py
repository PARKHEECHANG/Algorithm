n, limit = map(int, input().split())

lst = []

for i in range(n) :
    s, y = map(int, input().split())
    lst.append((s,y)) # 학생 정보 튜플로 리스트에 저장

# 정렬 순서 (학년 => 성별)
lst.sort(key = lambda x : x[1])
lst.sort(key = lambda x : x[0])

# 앞 학생과 뒤 학생 비교
num_room = 1 # 처음 방
num_stdnt = 1 # 처음 학생 수
for i in range(n-1) :
    if num_stdnt == limit : # 방이 꽉 차면
        num_room += 1 # 방 추가
        num_stdnt = 1 # 학생 수 초기화

    elif lst[i] == lst[i+1] : # 앞 학생과 뒤 학생이 같은 성별, 같은 학년
        num_stdnt += 1 # 모이기

    elif lst[i] != lst[i+1] : # 다른 학생
        num_room += 1 # 다른 방
        num_stdnt = 1 # 학생 수 초기화

print(num_room)