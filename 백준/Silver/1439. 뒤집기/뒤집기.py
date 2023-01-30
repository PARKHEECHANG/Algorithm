s = input()

lst = list(s)

num = lst[0] 
num_cnt = 1
num2_cnt = 0
isnum2 = False

for i in range(1,len(s)) :

    if isnum2 == False :
        if lst[i] != num :
            isnum2 = True
            num2_cnt += 1
    
    if isnum2 == True :
        if lst[i] == num :
            isnum2 = False
            num_cnt += 1

if num2_cnt <= num_cnt :
    print(num2_cnt)
else :
    print(num_cnt)
        