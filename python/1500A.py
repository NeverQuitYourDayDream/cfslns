# 1500A. Going Home
# Completed in 1903 ms 122100 KB
# 03/27/2021

__name__ = "__main__"

if __name__ == "__main__":

    n = int(input())
    nums = list(map(int, input().split())) 

    # let's put all of our sums in here
    sums = {}

    solved = False 

    for i in range(0, n):
        for j in range(0, i):

            if nums[i] + nums[j] in sums:
                a, b = sums[nums[i] + nums[j]]
            
                if i != a and i != b and j != a and j != b:
                    print("YES") 
                    print(i+1, j+1, a+1, b+1)
                    solved = True
                    break 

            else:
                # add nums[i] + nums[j] to sums
                sums[nums[i] + nums[j]] = [i, j]
        
        if solved:
            break

    if not solved:
        print("NO")
        
