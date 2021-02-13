# 710A. King moves
# Completed in 62 ms 300 kb

pos = [i for i in input()]
file = pos[0]
rank = pos[1]

if file == 'a':
    if rank == '1' or rank == '8':
        print(3)
    else:
        print(5)
elif file == 'h':
    if rank == '1' or rank == '8':
        print(3)
    else:
        print(5)
elif rank == '1':
    if file == 'a' or file == 'h':
        print(3)
    else:
        print(5)
elif rank == '8':
    if file == 'a' or file == 'h':
        print(3)
    else:
        print(5)
else:
    print(8)
