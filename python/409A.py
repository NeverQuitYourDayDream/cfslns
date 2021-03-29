# 409A. The Great Game
# Completed in 62 ms 300 kb
# 03/29/2021

a = input()
a_actions = [(a[i:i+2]) for i in range(0, len(a), 2)]

b = input() 
b_actions = [(b[i:i+2]) for i in range(0, len(b), 2)]

# print(a_actions, b_actions)

rock = "()"
paper = "[]"
scissors = "8<"

a_pts = 0
b_pts = 0

for i in range(len(a)//2):
    if a_actions[i] == rock:
        if b_actions[i] == scissors:
            a_pts += 1
        elif b_actions[i] == paper:
            b_pts += 1
        else:
            a_pts += 1
            b_pts += 1
    elif a_actions[i] == paper:
        if b_actions[i] == rock:
            a_pts += 1
        elif b_actions[i] == scissors:
            b_pts += 1
        else:
            a_pts += 1
            b_pts += 1
    else:
        # a_actions[i] == scissors
        if b_actions[i] == paper:
            a_pts += 1
        elif b_actions[i] == rock:
            b_pts += 1
        else:
            a_pts += 1
            b_pts += 1

if a_pts > b_pts:
    print("TEAM 1 WINS")
elif a_pts < b_pts:
    print("TEAM 2 WINS")
else:
    print("TIE")
