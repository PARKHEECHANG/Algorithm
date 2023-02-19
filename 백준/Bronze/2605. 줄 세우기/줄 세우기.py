n = int(input()) # 학생의 수

num_lst = list(map(int, input().split())) # 뽑은 번호

students = [0] * (n+1) # 학생 순서 리스트

# 그냥 교체 메소드..
def shift(now) :
    students[now], students[now-1] = students[now-1], students[now]

# 첫번쨰 학생
students[1] = 1 # 무조건 0번을 받는다.

# 그 다음 학생
# 뽑은 번호의 인덱스 + 1 == 학생 번호가 되는 것을 이해해야 함.
for idx in range(1, n) : # 두번째~끝
    students[idx + 1] = idx + 1 # 일단 줄 세우기
    num = num_lst[idx] # 뽑은 번호
    if num == 0 : # 뽑은 번호가 0이면 바꾸지 않고 그대로 줄 서면 된다.
        continue
    elif num > 0 : # 뽑은 번호가 1이상이면, 그만큼 앞으로 가야해요.
        now = idx+1
        for i in range(num) : # 뽑은 번호 만큼
            shift(now) # 앞사람과 교체
            now -= 1 # 교체 후 now의 위치는 그만큼 당겨짐.

for i in range(1, n+1) :
    print(students[i], end=' ')