def myFunc(a, b):
    if a > b:
        for j in range(2, b + 1, 1):
            if a % j == 0 and b % j == 0:
                return 0
        else:
            return 1
    elif a < b:
        for g in range(2, b + 1, 1):
            if a % g == 0 and b % g == 0:
                return 0
        else:
            return 1
    else:
        return 0
count = 0
num = int(input())
n = num // 2 + 1
for i in range(2, n, 1):
    x, y = i, num - i
    result = myFunc(x, y)
    if result == 1:
        count += 1
        print(x, y)
        
print(count)