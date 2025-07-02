import functions as funcs
n = 30000
divs = funcs.divcount(n)
nums = set(i for i in range(1,n+1))
abundant_nums = [i for i in range(n) if divs[i]>i]
abundant_nums.pop(0)
for i in range(len(abundant_nums)):
    for j in range(i, len(abundant_nums)):
        target = abundant_nums[i] + abundant_nums[j]
        if target in nums:
            nums.remove(target)
#print(abundant_nums)
print(nums)
print(sum(nums))
#print(abundant_nums)