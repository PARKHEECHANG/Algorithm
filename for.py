# 연속되는 네모 n칸의 합이 가장 클 때 의 값은?
lst = [[4,5,2,6,7,3,1],
       [2,9,9,6,1,6,7]]

n = int(input())
max = 0
def search(row):
    global max
    for i in range(len(lst[row])-n+1) :
        sum = 0
        for j in range(i, i+n) :
            sum += lst[row][j]
        if max < sum :
            max = sum

for i in range(len(lst)) :
    search(i)

print(max)


# 정수 n개 입력받고 패턴 존재 여부 출력하기
arr=[3,6,5,8,5,3,5,8,5,3,3,1,1,3]
n = int(input())
ptn = list(map(int, input().split()))

def search(idx) :
    for j in range(n):
        if arr[idx+j] != ptn[j]:
            return 0
    return 1

samePtn = 0

for i in range(len(arr) - n + 1):
    samePtn = search(i)
    if samePtn == 1 :
        print("1")
        break

if samePtn == 0 :
    print("0")
