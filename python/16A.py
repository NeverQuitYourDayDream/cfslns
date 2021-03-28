# 16A. Flag
# Completed in 124 ms 0 kb
# 03/28/2021

def solve(flag, rows):

    for i in range(rows):
        try:
            if len(set(flag[i])) != 1 or flag[i] == flag[i+1]:
                return "NO" 
        except IndexError:
            continue

    return "YES"

rows, cols = map(int, input().split())
flag = []
for row in range(rows):
    row = input()
    flag.append(row) 

print(solve(flag, rows))
