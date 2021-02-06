# 977A Wrong Subtraction 
# Completed in 62 ms 0 kb

n, k = map(int, input().split())
 
while k > 0:

    if n % 10 != 0:
        n = n - 1
    else:
        n = n // 10
        
    k = k - 1
 
print(n)
