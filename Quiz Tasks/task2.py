i = 0
nums = []
print("enter 5 nums:")
while i < 5:
    num = int(input())
    nums.append(num) 
    i += 1
print(nums)
nums = tuple(nums)
print(nums)
nums = set(nums)
print(nums)
