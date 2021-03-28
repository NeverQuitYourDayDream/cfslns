# 60A. Where Are My Flakes?
# Completed in 154 ms 0 kb
# 03/28/2021

n, m = map(int, input().split())

left, right = 1, n

for i in range(m):
    inp = input().split()
    if inp[2] == "left":
        right = min(right, int(inp[4]) - 1)
    else:
        left = max(left, int(inp[4]) + 1)
    
if left <= right:
    print(right - left + 1)
else:
    print(-1)
