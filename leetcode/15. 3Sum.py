"""
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def two_sum(self, nums, target, res, path):
        import copy
        path_copy = copy.deepcopy(path)
        # importing copy module
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                res.append(path + [nums[i], nums[j]])
                while i < j and nums[i] == nums[i + 1]:
                    i += 1
                while i < j and nums[j] == nums[j - 1]:
                    j -= 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
            path = path_copy

    def n_sum(self, nums, n, target, res, path):
        print(n, path, target)
        if n > len(nums):
            res = []

        if n == 2:
            self.two_sum(nums, target, res, path)
        else:
            for i, v in enumerate(nums):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                else:
                    self.n_sum(nums[i + 1:], n - 1, target - nums[i], res, path + [nums[i]])

    def FourSum(self, nums, target):
        result = []
        nums.sort()
        print(nums)
        print('---------------------')
        self.n_sum(nums, 4, target, result, [])
        return result


so = Solution()
print(so.FourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))
print('***********')
print(
[[-5,-4,-3,1]])
