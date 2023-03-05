def search(sm, lv, st) :
    global flag

    if flag == True :
        return
    
    if sm > 100 or lv > 7:
        return

    if sm == 100 and len(ans) == 7 and flag == False:
        flag = True
        ans.sort()
        for i in range(7) :
            print(ans[i])

    for i in range(st, 9) :
        ans.append(lst[i])
        search(sm + lst[i], lv+1, i+1)
        ans.pop()

lst = [0] * 9
for i in range(9) :
    lst[i] = int(input())

flag = False
ans = []
ans = search(0, 0, 0)