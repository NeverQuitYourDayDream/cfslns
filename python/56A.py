# 56A. Bar
# Completed in 124 ms 300 kb

n = int(input())
data = []
for i in range(n):
    inp = input()
    data.append(inp)
 
ages = [int(i) for i in data if i[0] in '1234567890']
drinks = [i for i in data if i not in ages]
alcoholic_drinks = ["ABSINTH", "BEER", "BRANDY", 
                    "CHAMPAGNE", "GIN", "RUM", 
                    "SAKE", "TEQUILA", "VODKA", 
                    "WHISKEY", "WINE"]
                    
underage = 0
alcoholic = 0
 
for i in ages:
    if int(i) < 18:
        underage += 1
 
for i in drinks:
    if i in alcoholic_drinks:
        alcoholic += 1
 
print(underage + alcoholic)
