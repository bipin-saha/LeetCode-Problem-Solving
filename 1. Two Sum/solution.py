#Problem
#https://leetcode.com/problems/two-sum/description/

# Solution

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in range(0, len(nums)):
            for num2 in range(num+1, len(nums)):
                if nums[num] + nums[num2] == target:

                    return [num, num2]