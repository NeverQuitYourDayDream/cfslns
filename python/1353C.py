# 1353C. Board Moves
# Completed in 233 ms 0 kb 
# 2/26/2021 

t = int(input()) 

while t > 0:
    n = int(input()) 
    
    moves = 0
    while n > 1:
        moves += (n*n - (n-2)*(n-2)) * (n//2)
        n -= 2
        
    print(moves)
    t -= 1
