"""
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def twoSumClosest(self, nums, target, res, origin, present):
        left, right = 0, len(nums) - 1
        while left < right:
            add_sum = nums[left] + nums[right]
            if add_sum == target:
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                res = origin
                break
            elif add_sum < target:
                left += 1
            else:
                right -= 1
            if abs(add_sum+present - origin) < abs(res - origin):
                res = add_sum+present
        return res

    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        res = float('inf')
        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                res = self.twoSumClosest(nums[i + 1:], target - v, res, target, v)
        return res


so = Solution()
so.threeSumClosest([-1, 2, 1, -4], 1)
