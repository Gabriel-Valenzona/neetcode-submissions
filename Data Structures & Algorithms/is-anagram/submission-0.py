class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # init hashmap - cound num of each unique character
        count_s = {}
        count_t = {}
        # iterate through and increment hashmap
        for c in s:
            if c in count_s:
                count_s[c] += 1
            else:
                count_s[c] = 1
            
        for c in t:
            if c in count_t:
                count_t[c] += 1
            else:
                count_t[c] = 1
        
        # compare the ASCII value of the two strings, then if they are equal it will return
        return t == s
        # because ASCII comparison takes into consideration edge cases like upper/lower cases we can directly compare like that