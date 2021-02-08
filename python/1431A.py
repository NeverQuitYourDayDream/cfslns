# 1431A Selling Hamburgers 

t = int(input())

while t > 0:
    n = int(input())
    coins = [int(coin) for coin in input().split()]
    m = min(coins)
    
    coins = list(filter(lambda x: x >= m, coins))
    print(len(coins) * m)
    t -= 1
