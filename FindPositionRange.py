# Input: nums = [3,7,7,8,8,10], target = 8
# Output: [3,4]
def FindPositionRange(nums: int, target: int):
    if len(nums) == 0:
        return [-1, -1]
    lp = leftBound(nums, target)
    rp = rightBound(nums, target) - 1
    if lp == len(nums)-1 or nums[lp] != target:
        return [-1, -1]
    return [lp, rp]

# the most important and difference between leftBound and rightBound is:
# nums[mid] >= target to find the biggest one which less than target.
# nums[mid] > target to find the lowest one which bigger than target.


def leftBound(nums: int, target: int):
    l = 0
    r = len(nums)-1
    while l < r:
        mid = (l+r)//2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    return l


def rightBound(nums: int, target: int):
    l = 0
    r = len(nums)-1
    while l < r:
        mid = (l+r)//2
        if nums[mid] > target:
            r = mid
        else:
            l = mid + 1
    return l


# print(FindPositionRange([3, 7, 7, 8, 8, 10], 8))
