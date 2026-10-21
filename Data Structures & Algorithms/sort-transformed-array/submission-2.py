class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def applyQuardraticForm(a, b, c, x):
            return (a*(x**2) + (b*x) + c)

        new_nums = []
        # convert every number
        for num in nums:
            new_nums.append(applyQuardraticForm(a,b,c,num))

        # sort ascending order
        return sorted(new_nums)

    # # make a math function to calculate
    # def applyQuardraticForm(self, a, b, c, x):
    #     return (a*(x**2) + (b*x) + c)