"""
A. Puzzle From the Future
https://codeforces.com/problemset/problem/1474/A
Completed in 155 ms 1200 kb.
"""

t = int(input())
 
while t > 0:
    n = int(input())
    
    a = []
    b = input()
    
    for i, c in enumerate(b):
        
        if i == 0:
            a.append('1')
        
        else:
            # find the current digit
            # to determine whether or not 
            # a cary-over occured
            last = int(b[i-1]) + int(a[i-1])
            if last == 2:
                if c == '0':
                    a.append('1')
                else:
                    a.append('0')
            elif last == 1:
                if c == '1':
                    a.append('1')
                else:
                    a.append('0')
            else:
                a.append('1')
                
    t -= 1
    print(''.join(a))
