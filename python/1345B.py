# 1345B. Card Construction

def cards(h):
    res = 0
    for i in range(1, h+1):
        res += 3*i - 1 
    return res

def solve(n):
    pyramids = 0
 
    i = 1
    while n > 0:
        if n < 2:
            break

        if cards(i) <= n and cards(i+1) > n:
            n -= cards(i)
            pyramids += 1
            i = 1
        else:
            i += 1        
        
    return pyramids
 
t = int(input())
while t > 0:
    n = int(input())
    print(solve(n))
    t -= 1
