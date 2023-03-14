for t_case in range(1, 11) :
    size, st = map(int, input().split())
    lst = list(map(int, input().split()))

    edges = [ [] for _ in range(101) ]
    visited = [0] * 101

    for i in range(0, size, 2) :
        parent, child = lst[i], lst[i+1]
        edges[parent].append(child)

    visited[st] = 1
    now_level = [st] # 현재 레벨 노드 리스트

    while 1 :
        next_level = [] # 다음 레벨 노드 리스트
        for i in range(len(now_level)) :
            now = now_level[i]
            for j in range(len(edges[now])) :
                next = edges[now][j]
                if visited[next] == 0 :
                    visited[next] = 1
                    next_level.append(next)

        if next_level : # 다음 레벨 노드 리스트 값으로 끝인지 아닌지 판단
            now_level = next_level
        if not next_level :
            break

    print(f'#{t_case} {max(now_level)}')