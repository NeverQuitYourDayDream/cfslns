# 1481A Space Navigation
# Completed in 77 ms 600 kb

t = int(input())
 
while t > 0:
    x, y = map(int, input().split())
    s = input()
    
    U = s.count("U")
    D = s.count("D")
    R = s.count("R")
    L = s.count("L")
    
    if x >= 0 and y >= 0:
        if R >= x and U >= y:
            print("YES")
        else:
            print("NO")
            
    elif x <= 0 and y >= 0:
        if L >= abs(x) and U >= y:
            print("YES")
        else:
            print("NO")
    
    elif x <= 0 and y <= 0:
        if L >= abs(x) and D >= abs(y):
            print("YES")
        else:
            print("NO")
    
    else:
        if R >= x and D >= abs(y):
            print("YES")
        else:
            print("NO")
    
    t -= 1
