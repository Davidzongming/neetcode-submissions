class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                mid = i
        if nums[l] < target and nums[mid] > target:
            r = mid
        elif nums[r] > target and nums[mid] < target:
            l = mid
        for i in range(l,r+1):
            mid = l+ (r - l)//2
            if nums[i] == target:
                return i
            elif target > nums[mid]:
                l = mid
            else:
                r = mid
        return -1