# 1201A. Important Exam
# Completed in 202 ms 1800 kb
# 3/5/2021

n, m = map(int, input().split()) 
answers = []
for i in range(n):
    inp = input()
    answers.append(inp)

scores = [int(i) for i in input().split()]
best = 0
for i in range(m):
    choices = [ans[i] for ans in answers]
    a = choices.count('A')
    b = choices.count('B')
    c = choices.count('C')
    d = choices.count('D')
    e = choices.count('E')
    best += max(a, b, c, d, e) * scores[i]

print(best)
