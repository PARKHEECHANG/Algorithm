list = input().split('-')

for i in range(len(list)):
    list[i] = sum(map(int, list[i].split('+')))

else:
    print(list[0] - sum(list[1:]))
