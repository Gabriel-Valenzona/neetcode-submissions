class Solution:
    def isValid(self, s: str) -> bool:
        # init stack
        stack = []

        # use hashmap to fetch matching opening bracket
        matching_pairs = {']': '[', ')': '(', '}': '['}

        for c in s:
            if c in matching_pairs:
                if stack and stack[-1] == matching_pairs[c]: # DID NOT GET
                    stack.pop() # DID NOT GET
                else: # DID NOT GET
                    return False # DID NOT GET
            else:
                stack.append(c)
        
        return True if not stack else False
        # worse case - o(n) time complexity because we have to iterate index by index in string
        # iterate through string, if open bracket is found then append its corresponding closed bracked to stack

        # once 