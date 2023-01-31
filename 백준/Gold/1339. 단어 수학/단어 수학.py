alpha = [ 0 for i in range(26)]
lst = []

# 입력
n = int(input())
for i in range(n):
    lst.append(input())

# 알파뱃 하나씩 환산하여 리스트에 저장
for i in range(n) :
    value = 10 ** (len(lst[i])-1)
    for j in lst[i] :
        alpha[ord(j)-65] += value
        value //= 10

# 내림차순 정렬
alpha.sort(reverse=True)

sum = 0
num = 9

# 높은 알파뱃 값 순으로 9~0 곱해주기
for i in alpha :
    sum += i * num
    num -= 1

print(sum)