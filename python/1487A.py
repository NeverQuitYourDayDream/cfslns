# 1487A. Arena
# Completed in 78 ms 0 kb

t = int(input()) 

while t > 0:
    n = int(input()) 
    levels = list(map(int, input().split()))

    levels = sorted(levels)

    ans = 0
    for i in levels:
        if i != levels[0]:
            ans += 1
    
    print(ans)
    t -= 1
