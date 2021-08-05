class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        start = 0 
        end  = len(s) - 1
        
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start, end = start + 1, end - 1
            
        return True     