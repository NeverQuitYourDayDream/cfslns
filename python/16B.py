# 16B. Burglar and Matches
# Completed in 156 ms 300 kb
# 03/28/2021

n, m = map(int, input().split()) 

matchboxes = []
for i in range(m):
    # boxes and matches
    a, b = map(int, input().split()) 

    #for i in range(a):
    #    matchboxes.append((1, b))

    matchboxes.append((a, b))

matchboxes = sorted(matchboxes, key=lambda x: x[1], reverse=True)

ans = 0
for box in matchboxes:
    if n > box[0]:
        n -= box[0]
        ans += box[0] * box[1]
    else:
        ans += n * box[1]
        break

print(ans)
