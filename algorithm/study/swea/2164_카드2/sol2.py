nums = [i for i in range(1, int(input()) + 1)]

while 1 != len(nums):
    nums.pop(0)
    nums.append(nums.pop(0))
print(*nums)