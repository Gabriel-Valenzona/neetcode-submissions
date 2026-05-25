class Solution:
    def isPalindrome(self, s: str) -> bool:
        # space complexity: o(1) regardless of string size, nothing is stored
        # time complexity: o(n) - at worse case, we iterate through the size of the string so the algorithm grows linearly 
        l = 0
        r = len(s) - 1

        while l < r: # when left pointer intersects with right then we know that entire string has been processed
            while l < r and not s[l].isalnum(s[l]): # move left pointer toward center until it reaches a alphanumeric
                l += 1
            while r > l and not s[r].isalnum(s[r]): # move right pointer toward center until it reaches a alphanumeric
                r += 1
            if s[l].lower() != s[r].lower():
                return False
        
        return True

        




                
