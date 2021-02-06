"""
1475 B. New Year's Number
Polycarp remembered the 2020-th year, and he is happy with the arrival of the new 2021-th year. 
To remember such a wonderful moment, Polycarp wants to represent the number n as the sum of a 
certain number of 2020 and a certain number of 2021.

For example, if:

n=4041, then the number n can be represented as the sum 2020+2021;
n=4042, then the number n can be represented as the sum 2021+2021;
n=8081, then the number n can be represented as the sum 2020+2020+2020+2021;
n=8079, then the number n cannot be represented as the sum of the numbers 2020 and 2021.
Help Polycarp to find out whether the number n can be represented as the sum of a certain 
number of numbers 2020 and a certain number of numbers 2021.

Completed in 155 ms 0 kb
"""

t = int(input())
 
while t > 0:
    
    n = int(input())
    q = n // 2020
    r = n % 2020
    
    if r <= q:
        print("YES")
    else:
        print("NO")
    
    t -= 1