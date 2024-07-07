#Problem
# https://leetcode.com/problems/single-number/submissions/1312934871/

#Solution
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = 0
        for x in nums:
            unique ^= x
        
        return unique