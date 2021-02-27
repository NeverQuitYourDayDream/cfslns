# 230A. Dragons
# Completed in 154 ms 300 kb
# 2/27/2021

s, n = map(int, input().split()) 

# store dragons' strength and bonus points
dragon_stats = []
for i in range(n):
    dragon = list(map(int, input().split())) 
    dragon_stats.append(dragon) 

# sort dragon_stats by strength
dragon_stats = sorted(dragon_stats, key=lambda x: x[0])

win = True
for i in range(n):
    if s > dragon_stats[i][0]:
        s += dragon_stats[i][1]
    else:
        win = False 
    
    if not win:
        break 

if win:
    print("YES")
else:
    print("NO")
