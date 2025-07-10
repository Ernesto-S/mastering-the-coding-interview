# 136 Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1

 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

class Solutions:
        
    def single_number_sorted(nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        print(nums)
        for i in range(1,len(nums),2):
            if nums[i] != nums[i-1]:
                return nums[i-1]
        return nums[len(nums)-1]

    def xor_single_number(nums: list[int]) -> int:
        xor = 0

        for num in nums:
            xor ^= num
        return xor
    

# print(Solutions.single_number_sorted([2,2,1]))

# print(Solutions.single_number_sorted([4,1,2,1,2]))

# print(Solutions.single_number_sorted([1]))



print(Solutions.xor_single_number([2,2,1]))

print(Solutions.xor_single_number([4,1,2,1,2]))

print(Solutions.xor_single_number([1]))
