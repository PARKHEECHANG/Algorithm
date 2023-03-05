def search(now) :
    target = -1
    for i in range(len(line)-1, -1, -1) :
        if line[i] > now :
            target = i

    return target

t = int(input())
for t_case in range(1, t+1) :
    lst = list(map(int, input().split()))

    line = []
    cnt = 0 # 물러난 걸음

    for i in range(1,21) :
        now = lst[i]
        target = search(now) # 키 큰 학생
        if target == -1 : # 자기보다 키 큰 학생이 없음
            line.append(now) # 그냥 서기
        else : # 자기보다 키 큰 학생이 있음
            line.append(now) # 일단 줄 서기

            # line.insert(target-1, now)
            tmp = line[-1] # 잠시 빼놓고
            for j in range(len(line)-1-1, target-1, -1) : # 뒤로 한칸 씩 밀기
                line[j+1] = line[j]
                cnt += 1
            line[target] = tmp # 그 자리에 세우기

    print(f'{t_case} {cnt}')
