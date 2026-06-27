class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1

        for i in range(len(s)):
            temp = s[r]
            s[r] = s[l]
            s[l] = temp
        
