class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        print("before loop")
        while l < r:
            # move l pointer to next valid char
            while l < r and not s[l].isalnum():
                l += 1
            # move r pointer to next valid char
            while l < r and not s[r].isalnum():
                r -= 1
            # evaluate if same
            print(f"l is {s[l]} and r is {s[r]}")
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True