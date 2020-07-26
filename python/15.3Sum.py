class Solution:
    def threeSum(self, nums):
        # Questions: are the numbers distinct?
        n, res = len(nums), []
        nums.sort()
        for i in range(0, n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lo, hi = i + 1, n - 1
            while lo < hi:
                s = nums[lo] + nums[hi] + nums[i]
                if s == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo, hi = lo + 1, hi - 1
                elif s > 0:
                    hi = hi - 1
                else:
                    lo = lo + 1
        return res