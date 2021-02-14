# 7A. Kalevitch and Chess
# Completed in 124 ms 300 kb

board = []
 
painted_ranks = 0
painted_files = 0
 
for i in range(8):
  rank = input()
  # the number of B in each rank (row)
  painted = rank.count('B')
  if painted == 8:
    painted_ranks += 1
  board.append(rank)
 
# find the number of files
for i in range(8):
  x = 0
  for j in range(8):
    if board[j][i] == 'B':
      x += 1
  
  if x == 8:
    painted_files += 1
    
if painted_ranks == 8:
    print(8)
else:
    print(painted_files + painted_ranks)
