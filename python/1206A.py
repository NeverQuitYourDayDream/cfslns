# 1206A. Choose Two Numbers
# Completed in 62 ms 300 kb

n = int(input())
A = [int(i) for i in input().split()]
m = int(input())
B = [int(i) for i in input().split()]
ans = []

def solve():
    for i in range(0, n):
        for j in range(0, m):
            if A[i] + B[j] not in A and A[i] + B[j] not in B:
                return str(A[i]) + " " + str(B[j])
            
print(solve())
