#Problem
#https://leetcode.com/submissions/detail/1312801957/

#Solution
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if list(str(x)) == list(str(x))[::-1]:
            return True
        else:
            return False