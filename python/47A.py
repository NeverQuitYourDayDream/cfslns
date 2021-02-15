# 47A. Triangular Numbers
# Complted in 124 ms 0 kb

n = int(input())
 
x = 1
while x * (x+1) / 2 < n:
    x += 1
 
if x * (x+1) / 2 == n:
    print("YES")
else:
    print("NO")
