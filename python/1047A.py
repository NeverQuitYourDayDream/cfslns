# 1047A. Little C loves 3!
# Completed in 62 ms 0 kb

n = int(input())

# simplest solution has the form 1, 1, x, where x = n - (1 + 1) = n - 2
# if x % 3 != 0 then return 1, 1, x
# else we decrease x by 1 and increase b by 1
# if x % 3 != 0 and b % 3 != 0 then return 1, b, x
# else continue

def solve(n):
  a, b = 1, 1
  if (n - 2) % 3 != 0:
    return str(a)  + " " + str(b) + " " +  str(n - 2)
  else:
    c = 2
    while (n - c) % 3 == 0:
      if b % 3 == 0:
        continue
      else:
        c += 1
        b += 1
        n = n - c
    return str(a) + " " + str(b) + " " + str(n)
 
print(solve(n))
