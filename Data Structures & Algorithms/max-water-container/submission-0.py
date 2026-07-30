class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # (r - l) * min(height1, height2)
        l = 0
        r = 0
        A = 0
        while l < len(heights):
            r = l + 1
            while r < len(heights):  
                A = max(A, (r - l) * min(heights[l], heights[r]))
                r += 1
            l += 1
        return A
