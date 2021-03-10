# 1495A. Diamond Miner
# Completed in 670 ms 5700 kb
# 3/10/2021

from math import sqrt

t = int(input())
for i in range(t):
    n = int(input()) 
    x_axis = []
    y_axis = []
    
    for i in range(2*n):

        x, y = map(int, input().split()) 
        x, y = abs(x), abs(y)

        if x == 0:
            y_axis.append(y)
        else:
            x_axis.append(x)
    
    # the total distance is minimized by pairing
    # the largest xs with the largest ys
    x_axis = sorted(x_axis)
    y_axis = sorted(y_axis) 

    total = 0
    for i in range(n):
        total += sqrt(x_axis[i]**2 + y_axis[i]**2)
    
    print(total)
