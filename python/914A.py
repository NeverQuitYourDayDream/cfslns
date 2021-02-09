# 914A. Perfect Squares
# Completed in 93 ms 300 kb

import math
 
n = int(input())
 
nums = [int(i) for i in input().split()]
 
ans = -1_000_000 
for i in nums:
  if i < 0:
    if i > ans:
      ans = i
  else:
    if math.sqrt(i) != int(math.sqrt(i)) and i > ans:
      ans = i
 
print(ans)
