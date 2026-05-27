# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # init L and R pointer
        L, R = 0, n
        # loop that terminates when number has been guessed properly - L pointer overlapped with R pointer
        while True:
            # calculate mid-point index
            mid = (L + R) // 2
            # adjust L or R pointer depending on guess function return
            guess_result = guess(mid)
            # if guess higher than the number then
            if guess_result > 0:
                L = mid + 1
            elif guess_result < 0:
                R = mid - 1
            else:
                return mid