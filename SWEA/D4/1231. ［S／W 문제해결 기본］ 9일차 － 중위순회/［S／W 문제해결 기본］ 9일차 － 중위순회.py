def inorder(v) :
    if v > n :
        return
    inorder(2*v)
    print(st_lst[v],end='')
    inorder(2*v+1)
 
for t_case in range(1, 11) :
    n = int(input()) # 정점 수
 
    lst = [''] * n # input 리스트
    edges = [ [0] * 2 for _ in range(n+1) ] # 0 : 왼쪽, 1 : 오른쪽
    st_lst = [''] * (n+1)
 
    for i in range(n) : # 줄 입력
        lst[i] = list(input().split())
 
    for i in range(n) :
        node, st = lst[i][0], lst[i][1]  # 노드 번호, 노드 문자
        node = int(node)
        st_lst[node] = st
        if len(lst) == 3 :
            edges[node][0] = int(lst[i][2]) # 왼쪽 자식 번호
        elif len(lst) == 4 :
            edges[node][0] = int(lst[i][2]) # 왼쪽 자식 번호
            edges[node][1] = int(lst[i][3]) # 오른쪽 자식 번호
 
    print(f'#{t_case}',end=' ')
    inorder(1)
    print()