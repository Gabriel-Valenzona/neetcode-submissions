class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count_c = 0
        g_pointer = 0
        s_pointer = 0
        g_sort = sorted(g)
        s_sort = sorted(s)

        while g_pointer < len(g) and s_pointer < len(s):
            if g_sort[g_pointer] <= s_sort[s_pointer]:
                count_c += 1
                g_pointer += 1
                s_pointer += 1
                print(f"fed: {count_c} and g point is {g_pointer} and s point is {s_pointer}")
            elif g[g_pointer] > s[s_pointer]:
                s_pointer += 1
                print(f"s point is {s_pointer}")
            
        return count_c
