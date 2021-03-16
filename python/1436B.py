# 1436B. Prime Squares 
# Completed in 140 ms 0 kb
# 03/15/2021

def prime_square(n):
    result = []
    result.append([1] + [0]*(n-2) + [1])
    index = 0

    for i in range(0, n-1):
        row = [0] * n
        row[index] = 1
        row[index+1] = 1
        result.append(row)
        index += 1

    return result

t = int(input())
for i in range(t):
    n = int(input())
    square = prime_square(n)
    for row in square:
        print(*row)
