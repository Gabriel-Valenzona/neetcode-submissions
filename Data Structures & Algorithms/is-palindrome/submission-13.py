class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # move l pointer to next valid char
            while l < r and not s[l].isalnum():
                l += 1
            # move r pointer to next valid char
            while l < r and not s[r].isalnum():
                r += 1
            # evaluate if same
            if s[l] == s[r]:
                return False
        
        return True