"""
919B. Perfect Number

We consider a positive integer perfect, if and only if the sum of its digits is exactly 10. 
Given a positive integer k, your task is to find the k-th smallest perfect positive integer.

Input
A single line with a positive integer k (1 ≤ k ≤ 10000).

Output
A single number, denoting the k-th smallest perfect integer.

Completed in 1325 ms 0 kb.
"""

k = int(input())
 
pnums = []
 
def digsum(n):
    dsum = 0
    while n > 0 and dsum < 11:
        dsum += (n % 10)
        n = n // 10
    return dsum
    
i = 19
count = 0
 
while True:
    if digsum(i) == 10:
        count += 1
        
    if count == k:
        print(i)
        break
    
    i += 9
