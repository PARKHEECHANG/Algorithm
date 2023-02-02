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
