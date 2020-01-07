"""
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
7*7 = 49
"""


class Solution:
    def maxArea(self, height):
        best = -1
        i, j = 0, len(height) - 1
        while i < j:
            best = max(best, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return best


so = Solution()
print(so.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
