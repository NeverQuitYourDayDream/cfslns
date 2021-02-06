"""
102B. Sum of Digits

Having watched the last Harry Potter film, little Gerald also decided to practice magic. 
He found in his father's magical book a spell that turns any number in the sum of its digits. 
At the moment Gerald learned that, he came across a number n. 
How many times can Gerald put a spell on it until the number becomes one-digit?

Input
The first line contains the only integer n (0 ≤ n ≤ 10100000). It is guaranteed that n doesn't contain any leading zeroes.

Output
Print the number of times a number can be replaced by the sum of its digits until it only contains one digit.

Completed in 1870 ms 300 kb.
"""

n = int(input())

def solve(n):
    c = 0
    while n > 9:
        n = sum(map(int, str(n)))
        c += 1
        
    if n == 0:
        return 0
    else:
        return c
    
print(solve(n))