# 1462A Favorite Sequence
# Completed in 77 ms 300 kb

t = int(input())
 
while t > 0:
    n = int(input())
    nums = [int(i) for i in input().split()]
    restored = []
    
    while nums:
        restored.append(nums[0])
        del nums[0]
        nums.reverse()
    
    print(' '.join(str(i) for i in restored))
    
    t -= 1
