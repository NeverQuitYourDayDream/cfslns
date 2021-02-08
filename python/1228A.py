# 1228A Distinct Digits
# Completed in 62 ms 0 kb

def ud(x):
    if len(str(x)) == len(set(str(x))):
        return True
    return False
    
def solve(l, r):
    ans = 0
    for i in range(l, r+1):
        if ud(i):
            return i
            ans += 1
            break
    
    if ans == 0:
        return -1

l, r = map(int, input().split())
print(solve(l, r))
