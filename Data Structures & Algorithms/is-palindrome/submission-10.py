class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        for c in s:
            if s[l] != s[r]:
                return False
        
        return True