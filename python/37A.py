# 37A. Towers
# Completed in 154 ms 300 kb

bars = int(input())
bar_lengths = [int(i) for i in input().split()]
 
heights = []
for length in set(bar_lengths):
    heights.append(bar_lengths.count(length))
 
print(max(heights))
print(len(set(bar_lengths)))
