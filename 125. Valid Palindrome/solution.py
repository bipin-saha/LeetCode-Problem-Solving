#Problem
#https://leetcode.com/problems/valid-palindrome/submissions/1313813604/

#Solution
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cl = []

        for c in s:
            if c.isalnum():
                cl.append(c.lower())
               
        if cl == cl[::-1]:
            return True
        else:
            return False


        