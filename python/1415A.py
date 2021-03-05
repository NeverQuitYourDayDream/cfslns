# 1415A. Prison Break
# Completed in 170 ms 0 kb
# 3/5/2021

t = int(input()) 
for i in range(t):
    n, m, r, c = map(int, input().split()) 
    # the longest distance is just the manhattan distance
    # check manhattan distances from all 4 corners of the 
    # grid
    print(max(abs(n-r)+abs(m-c), abs(1-r)+abs(1-c), abs(n-r)+abs(1-c), abs(1-r)+abs(m-c)))
    
