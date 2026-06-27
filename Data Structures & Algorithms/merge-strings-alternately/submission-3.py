class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1, w2 = 0, 0
        final_s = ""
        
        if not word1:
            return word1
        elif not word2:
            return word2

        while w1 < len(word1) and w2 < len(word2):
            final_s += word1[w1]
            final_s += word2[w2]
            w1 += 1
            w2 += 1
        
        while w1 < len(word1):
            final_s += word1[w1]
            w1 += 1

        while w2 < len(word2):
            final_s += word2[w2]
            w2 += 1
        
        return final_s
