for t_case in range(1, 11) :
    n, pwd = map(str, input().split()) # 문자열의 길이, 비밀번호
    stack = []

    pwd = list(map(int, str(pwd)))

    while pwd :
        tmp = pwd.pop(0)

        if stack :
           if stack[-1] != tmp :
                stack.append(tmp)
           elif stack[-1] == tmp :
                stack.pop()

        else :
            stack.append(tmp)

    print(f'#{t_case}',end=' ')
    for i in range(len(stack)) :
        print(stack[i],end='')
    print()

