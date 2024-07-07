#Problem 
#https://leetcode.com/submissions/detail/1312784575/

#Solution
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])
        
