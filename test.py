nums = [1, 2, 0, 3, 3, 3, 0, 3, 5, 2, 2]
# nums = [1, 2, 3]

# print(max(set(nums), key=nums.count))
#
# set_nums = set(nums)
# print("False" if len(nums) == len(set_nums) else "True")
for i in nums:
    if i == 0:
        nums.remove(i)
        nums.append(i)
print(nums)

print(nums[::-1])