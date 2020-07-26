

def findPairWithGivenSum(nums, target):
    target = target - 30
    hash = {}
    max_pair = []
    for i in range(len(nums)):
        if target - nums[i] in hash:
            max_pair = [hash[target - nums[i]], i]
        hash[nums[i]] = i
    return max_pair

if __name__ == '__main__':
    print(findPairWithGivenSum([20, 50, 40, 25, 30, 10], 90))