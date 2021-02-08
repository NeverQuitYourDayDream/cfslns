# 869B. The Eternal Immortality

a, b = map(int, input().split())

def solve(a, b):
    if a == b:
        return 1
    elif a > b:
        return 0
    else:
        ld = 1
        for i in range(a + 1, b + 1):
            ld = (ld * i%10) % 10
            if ld == 0:
                break
    
    return ld

print(solve(a, b))
