# 1352C. K-th not divisible by N
# Completed in 62 ms 0 kb

t = int(input())

while t > 0:
    n, k = map(int, input().split())
  
    # c represents the amount we shift our answer forward
    # skip c numbers since those will be divisible by n
    # k-th positive integer plus c will be the answer
  
    # c is (k-1) divided by (n-1) rounded down (floor)
    c = (k-1) // (n-1)
    print(k + c)
    t -= 1
  
