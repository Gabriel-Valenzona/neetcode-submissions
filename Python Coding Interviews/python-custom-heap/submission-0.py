import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []
    # populate the heap with tuples (priority, real value)
    for num in nums:
        heapq.heappush(max_heap, (-num, num))
    
    res = []
    # append to new list in desired order
    while max_heap:
        res.append(heapq.heappop(max_heap)[1])
    
    # return reverse sorted
    return res


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
