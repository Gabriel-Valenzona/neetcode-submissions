class Solution:
    def isValid(self, s: str) -> bool:
        # init stack - contains unclosed parenthesis
        stack = []
        p_pairs = {'}': '{', ']':'[', ')':'('}
        # iterate through string - o(n) best time and space complexity
        for c in s:
            # condition 1 - if closed bracket, check if top of stack matches pair
            if c in p_pairs:
                # if not equal, return False
                if stack[-1] != p_pairs[c]:
                    return False
                stack.pop()
            # condition 2 - if open bracket, append to stack                
            else:
                stack.append(c)

        # T if empty, F if populated
        return not stack