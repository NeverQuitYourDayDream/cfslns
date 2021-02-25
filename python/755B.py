# 755B. PolandBall and Game
# Completed in 140 ms 2000 kb

n, m = map(int, input().split()) 

poland_words = []
enemy_words = []
shared_words = []
only_poland_words = []
only_enemy_words = []

for i in range(n):
    word = input() 
    poland_words.append(word)

for i in range(m):
    word = input()  
    enemy_words.append(word) 

shared_words = [word for word in poland_words if word in enemy_words]
only_poland_words = [word for word in poland_words if word not in shared_words]
only_enemy_words = [word for word in enemy_words if word not in shared_words] 

# print(shared_words)
# print(only_poland_words)
# print(only_enemy_words)

if len(shared_words) % 2 != 0:
    if len(only_poland_words) + len(shared_words) // 2 + 1 > len(only_enemy_words) + len(shared_words) // 2: 
        print("YES")
    else:
        print("NO")
else:
    if len(only_poland_words) > len(only_enemy_words): 
        print("YES")
    else:
        print("NO")
        
