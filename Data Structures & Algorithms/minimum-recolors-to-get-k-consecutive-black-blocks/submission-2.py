class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # w's in the inital window of size kk
        white_count = blocks[:k].count('W')
        min_recolors = white_count

        for i in range(k, len(blocks)):
            # add element entering window from right
            if blocks[i] == 'W':
                white_count += 1
            # add element entering window from left
            if blocks[i-k] == 'W':
                white_count -= 1

            # update min 
            min_recolors = min(white_count, min_recolors)

        return min_recolors

        