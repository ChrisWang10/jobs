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
                if tuple(path+[nums[i], nums[j]]) not in res:
                    res.append(tuple(path + [nums[i], nums[j]]))
                i += 1
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
            path = path_copy

    def n_sum(self, nums, n, target, res, path):
        if n > len(nums):
            res = []

        if n == 2:
            self.two_sum(nums, target, res, path)
        else:
            for i, v in enumerate(nums):
                self.n_sum(nums[i + 1:], n - 1, target - nums[i], res, path + [nums[i]])

    def threeSum(self, nums):
        result = []
        nums.sort()
        self.n_sum(nums, 3, 0, result, [])
        return [list(item) for item in list(set(result))]
        # return result

so = Solution()
print(so.threeSum([0, 0, 0, 0]))
