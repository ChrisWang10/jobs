"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


def dfs(to_close, to_open, res, path, n):
    if to_close == 0 and to_open == 0:
        print(path)
        res.append(path)
    else:
        if 0 < to_open <= n:
            dfs(to_close + 1, to_open - 1, res, path + '(', n)
        if 0 < to_close <= n:
            dfs(to_close - 1, to_open, res, path + ')', n)


def my_approach(n):
    res = []
    dfs(0, n, res, '', n)
    print(res)


class Solution:
    def dfs(self, need_open, need_close, res, path, n):
        if need_close == 0 and need_open == 0:
            res.append(path)
            return
        if n >= need_open > 0:
            self.dfs(need_open - 1, need_close + 1, res, path + '(', n)
        if n >= need_close > 0:
            self.dfs(need_open, need_close - 1, res, path + ')', n)

    def generateParenthesis(self, n: int):
        res = []
        self.dfs(n, 0, res, '', n)
        print(res)


# so = Solution()
# so.generateParenthesis(3)
my_approach(3)
