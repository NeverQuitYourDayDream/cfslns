# 1468E. Four Segments
# Completed in 61 ms 0 kb

t = int(input())
while t > 0:
    segments = [int(i) for i in input().split()]
    segments = sorted(segments)
    return (segments[0] * segments[2])
    print(solve(segments))
    t -= 1


