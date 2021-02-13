# 6A. Triangle
# Completed in 124 ms 0 kb

sticks = [int(i) for i in input().split()]
sticks = sorted(sticks)
a = sticks[0]
b = sticks[1]
c = sticks[2]
d = sticks[3]
 
def solve(a, b, c, d):
    if a+b > c or b+c > d:
        return "TRIANGLE"
    if a+b == c or b+c == d:
        return "SEGMENT"
    
    return "IMPOSSIBLE"
 
print(solve(a, b, c, d))
