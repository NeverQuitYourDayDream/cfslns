# 661C. Array Sum

import sys
def get_list():
    return list(map(int, sys.stdin.readline().strip().split()))
nums = get_list()
print(sum(nums))

# print(sum([input().split()]))
