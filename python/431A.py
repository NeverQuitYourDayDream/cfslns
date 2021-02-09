# 431A. Black Square
# Completed in 62 ms 300 kb

import sys
 
 
def get_int():
    return map(int, sys.stdin.readline().strip().split())
 
 
a, b, c, d = get_int()
 
 
def get_str():
    return sys.stdin.readline().strip()
 
 
s = get_str()
 
print(s.count("1") * a 
    + s.count("2") * b 
    + s.count("3") * c 
    + s.count("4") * d)
