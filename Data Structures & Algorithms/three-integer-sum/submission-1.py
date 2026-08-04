class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sortL = sorted(nums)
        for i in range(len(sortL)):
            l = i+1
            r = len(sortL) - 1
            if i > 0 and sortL[i] == sortL[i-1]:
                continue
            while l < r:
                total = sortL[i] + sortL[l] + sortL[r]
                if total == 0:
                    res.append([sortL[l], sortL[r], sortL[i]])
                    l += 1
                    while sortL[l] == sortL[l - 1] and l < r:
                        l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res

