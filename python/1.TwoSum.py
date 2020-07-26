class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        numSet = dict()

        for i, v in enumerate(nums):
            if (target - v) not in numSet:
                numSet[v] = i
            else:
                return [numSet[target - v], i]